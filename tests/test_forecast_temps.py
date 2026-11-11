import importlib.machinery
import importlib.util
import json
import re
import unittest
from pathlib import Path
from unittest.mock import patch


TEMP_LINE_RE = re.compile(r"▼ (-?\d+)ºC \|\| ▲ (-?\d+)ºC")


MODULE_PATH = Path(__file__).resolve().parents[1] / "wthr"
LOADER = importlib.machinery.SourceFileLoader("wthr_module", str(MODULE_PATH))
MODULE_SPEC = importlib.util.spec_from_loader(LOADER.name, LOADER)
if MODULE_SPEC is None:
    raise RuntimeError(f"Could not load module: {MODULE_PATH}")
wthr = importlib.util.module_from_spec(MODULE_SPEC)
LOADER.exec_module(wthr)


class FakeResponse:
    def __init__(self, payload):
        self._payload = payload

    @property
    def text(self):
        return json.dumps(self._payload)


def make_payload(mins, maxs):
    return {
        "daily": [
            {"temp": {"min": lo, "max": hi}, "weather": [{"main": "Clear"}]}
            for lo, hi in zip(mins, maxs)
        ]
    }


class ForecastTemperatureTests(unittest.TestCase):
    def test_forecast_temperatures_match_api_values(self) -> None:
        mins = [21.9, 20.0, -2.5, 0.0, 15.2, 30.7, -0.4, 9.9]
        maxs = [25.1, 22.0, 1.5, 3.0, 18.8, 33.3, 2.6, 12.4]
        with patch.object(
            wthr.requests, "get", return_value=FakeResponse(make_payload(mins, maxs))
        ):
            wthr.LAT, wthr.LON = "0", "0"
            packages = wthr.get_daily_forecast()
        shown = [TEMP_LINE_RE.search(pkg[12]).groups() for pkg in packages]
        shown_mins = [int(lo) for lo, _ in shown]
        shown_maxs = [int(hi) for _, hi in shown]
        self.assertEqual(shown_mins, [int(v) for v in mins])
        self.assertEqual(shown_maxs, [int(v) for v in maxs])


if __name__ == "__main__":
    unittest.main()
