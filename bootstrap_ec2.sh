#!/bin/bash

sudo apt-get update
sudo apt-get install -y build-essential python-dev python3-dev python3-pip virtualenvwrapper htop

export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

mkvirtualenv -a /opt/ppp -p python3 ppp
pip install -r requirements.txt
pip install -e .
