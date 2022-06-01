# wthr
*The current weather and temperature right from your terminal.*
<br><br>

<p align="center">  
  <img width="772" src="https://i.imgur.com/S0pD4ji.png">
</p>
<br>

## Installation

> Create an [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) account  and get a free API key. <br>You will be asked for the key the first time you run [wthr](https://github.com/Julynx/wthr).<br>

> Please note that [OpenWeatherMap](https://home.openweathermap.org) may take several minutes to activate newly created keys.<br>They will appear as invalid to [wthr](https://github.com/Julynx/wthr) during that time.

1) Download the latest version of [wthr](https://github.com/Julynx/wthr) from this repository:
```
git clone https://github.com/Julynx/wthr
cd wthr
```

2) Install the dependencies:
```
pip3 install geopy cursor requests
```

3) Run the following commands to install [wthr](https://github.com/Julynx/wthr) in your `/usr/bin/` directory:
```
sudo chmod +x wthr
sudo cp wthr /usr/bin/
```

The program can now be ran from a terminal with the `wthr` command.
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
  --verbose        Prints debug information whenever an API
  -v               call fails due to a key error.
```
