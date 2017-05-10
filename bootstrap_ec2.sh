#!/bin/bash

sudo apt-get install -y build-essential python3-dev python3-pip htop
sudo pip3 install virtualenvwrapper
source virtualenvwrapper.sh
mkvirtualenv -a /opt/ppp -p python3 ppp
pip install -r requirements.txt
pip install -e .
