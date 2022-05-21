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
The first step is to download the latest version of wthr from this repository:
```
git clone https://github.com/Julynx/wthr
cd wthr
```
Now, create an OpenWeatherMap account [here](https://home.openweathermap.org/users/sign_up) and get a free API key.

Then, open the file `wthr` and enter your API key:
```
...
api_key = "Your API key here"
...
```
The final step is to install the file in your `/usr/bin/` directory:
```
sudo chmod +x wthr
sudo cp wthr /usr/bin/
```
The program can now be ran from a terminal with the command `wthr`.
<br><br>

## Usage
```
Displays weather information from openweathermap.
Please, make sure to get your API key and paste it
at line 19 of this file: 'api_key = YOUR_API_KEY_HERE'.

  Usage:           wthr [LOCATION] [OPTIONS] ...
  Example:         wthr Dubai

  --mode=default   Equivalent to ommiting the '--mode' flag.
                   Shows the current weather for the location.
  --mode=forecast  Displays an 8-day forecast for the location,
                   including minimum and maximum temperatures
```
