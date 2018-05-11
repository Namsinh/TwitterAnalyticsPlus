# Twitter Analytics+

This application aims to provide the user with insights on the nature of content being published by the people they follow.
The application is still in the development stage. Note that there isn't much user feedback in the GUI, so it will take some time for the insights to load. This is due to the large number of twitter users and tweets that the application must work through.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Run with Docker

NOTE: If you don't have Tkinter installed already, you must install it. It can't be installed with docker.

```
$ docker image build -t test .
```

Run script
```
$ docker container run --rm -it test
```

Run GUI
```
$ docker container run --rm -it main
```

### Setting up the environment

The following dependencies must be installed in your machine in order to compile the application:

* Python 2.4.0+
* NOTE: If you're not using the docker container to build and run the code, Python 2 must be used. Python 3 will not work.
* <a href="https://github.com/tweepy/tweepy/" target="_blank">Tweepy</a>: A Python library for accessing Twitter API
> To install Tweepy package using pip run the following command in your terminal:

```
$ pip install tweepy
```

* Google Cloud Natural Language
> To install Google Cloud Language run the following command in your terminal:
```
$ pip install --upgrade google-cloud-language
```
A personal access key for Google Services must be obtained.

Further instructions on how to install Google Cloud Language library and set up an access key visit can be found at https://cloud.google.com/natural-language/docs/reference/libraries#client-libraries-install-php

* <a href="http://www.nltk.org">Natural Language Toolkit</a>: To install the package run the following command in the terminal:
```
$ sudo pip install -U nltk
```

### Running and testing the application

GUI Version: Run `./main.py` in python.

Script Version (with extra metrics): ./test.py in python
