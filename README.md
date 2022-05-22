# wthr
*The current weather and temperature right from your terminal.*
<br><br>

<p align="center">  
  <img width="772" src="https://i.imgur.com/GyVUxL2.png">
</p>
<br>

## Dependencies
wthr uses [geopy](https://pypi.org/project/geopy/), [cursor](https://pypi.org/project/cursor/) & [requests](https://pypi.org/project/requests/), which can be installed by executing:
```
pip3 install geopy cursor requests
```
It has been tested with Python 3.8.10, results may vary if other versions are used.
<br><br>

## Installation

> Create an [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) account  and get a free API key. <br>You will be asked for the key the first time you run [wthr](https://github.com/Julynx/wthr).

Download the latest version of [wthr](https://github.com/Julynx/wthr) from this repository:
```
git clone https://github.com/Julynx/wthr
cd wthr
```

Then, run the following commands to install [wthr](https://github.com/Julynx/wthr) in your `/usr/bin/` directory:
```
sudo chmod +x wthr
sudo cp wthr /usr/bin/
```

The program can now be ran from a terminal with the command `wthr`.
<br><br>

## Usage
```
  Displays weather information from openweathermap.

  Usage:           wthr [LOCATION] [OPTIONS] ...
  Example:         wthr Dubai

  --mode=default   Equivalent to ommiting the '--mode' flag,
  -d               shows the current weather for the location.
  --mode=forecast  Displays an 8-day forecast for the location,
  -f               including minimum and maximum temperatures.
```
