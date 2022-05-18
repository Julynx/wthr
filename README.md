# wthr
*The current weather and temperature right from your terminal.*
<br><br>

<p align="center">  
  <img width="772" src="https://i.imgur.com/sICDUAw.png">
</p>
<br>

## Dependencies
wthr uses [geopy](https://pypi.org/project/geopy/) & [cursor](https://pypi.org/project/cursor/), which can be installed by executing:
```
pip3 install geopy cursor
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
nano wthr
```
```
...
api_key = "Your API key here"
...
```
The final step is to install the file in your `/usr/bin/` directory:
```
chmod +x wthr
```
```
sudo cp wthr /usr/bin/
```
The program can now be ran from a terminal with the command `wthr`.
<br><br>

## Usage
Execute the following command to check the weather of the location passed as argument: 
```
wthr <location>
```
For example:
```
wthr Dubai
```
