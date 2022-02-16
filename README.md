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
pip3 install geopy
pip3 install cursor
```
It has been tested with Python 3.8.10, results may vary if other versions are used.
<br><br>

## Installation
The following commands will download the latest version of wthr from this repository 
and install it in your `/usr/bin/` directory:
```
git clone https://github.com/Julynx/wthr
cd wthr
chmod +x wthr
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
