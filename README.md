## Balert :loudspeaker:

Balert is for all the lazy people (like me :bowtie: ) who often miss desktop notifications. Balert 
will say it clear and loud whenever your battery status goes below a default critical level or the level decided by you! 

| Build Status | Version | Downloads | Python   |
| ------------ |---------|-----------|----------|
| [![Build Status](https://travis-ci.org/tushar-rishav/balert.svg?branch=master)](https://travis-ci.org/tushar-rishav/balert)|[![PyPI version](https://badge.fury.io/py/balert.svg)](http://badge.fury.io/py/balert)| [![PyPi downloads](https://img.shields.io/pypi/dm/Balert.svg)](https://pypi.python.org/pypi/Balert)|[![PyPI](https://img.shields.io/pypi/pyversions/Balert.svg)](https://pypi.python.org/pypi/Balert)
### [Demo](https://cloud.githubusercontent.com/assets/7397433/9695992/263ad662-5386-11e5-9066-e1714fb2aa0b.gif)
![balert](https://cloud.githubusercontent.com/assets/7397433/9695992/263ad662-5386-11e5-9066-e1714fb2aa0b.gif)


### Installation

##### Build from tar files
```sh
	wget "https://pypi.python.org/packages/source/B/Balert/Balert-1.1.8.tar.gz"
	tar xzvf Balert-1.1.8.tar.gz
	cd Balert-1.1.8
	python setup.py install
```
##### Build from source
```sh
	git clone https://github.com/tushar-rishav/balert.git Balert
	cd Balert
	python setup.py install
```
##### Using pip
```sh
	pip install Balert
```
After installation is done successfully, run any combinations of below command in your terminal once for initial setup and then we are done! If you want to use the default setup then just run  ``` balert ``` in terminal. 

###Default config:
	language: English
	rate    : 150
	charge  : 20 (in percentage)
    msg     : ""
    vol     : 1.0

###Options
```sh
usage: main.py [-h] [-r RATE] [-v VOL] [-l LANG] [-m MSG] [-c CHARGE] [-s]

Listen the voice of your battery whenever she is low!

optional arguments:
  -h, --help            show this help message and exit
  -r RATE, --rate RATE  Rate of speaking.(100-200)
  -v VOL, --vol VOL     Volume of speaking.(1.0)
  -l LANG, --lang LANG  Language speaking
  -m MSG, --msg MSG     Alert message of your own
  -c CHARGE, --charge CHARGE
                        Decide the critical charge level
  -s, --show            Show the currently set config


```

### Usage

##### Set language
To set the language eg. hindi, english , tamil. Default one is english
```sh

balert -l hindi

```

##### Set rate of speaking
```sh
balert -r 100

```

##### Set your custom alert message
```sh

balert -m "Delta is the state of mind"

```

##### Set custom charge level. 
If the battery level is below this critical level then it will give voice alert

```sh
balert -c 30

```
##### View the set configuration
```sh
balert -s
```

##### Get help
```sh
balert -h
```
##### Example
```sh
balert -m "Hey,Lazy dog " -c 25
```
When you run the above code, you've set "Hey,Lazy dog" as your custom message and 25 as your critical charge level.


### Contributions
Have an idea to make it better? Go ahead! I will be happy to see a pull request from you! :blush:

### License
![gpl](https://cloud.githubusercontent.com/assets/7397433/9025904/67008062-3936-11e5-8803-e5b164a0dfc0.png)
