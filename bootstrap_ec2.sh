#!/bin/bash

sudo apt-get update
sudo apt-get install -y build-essential python-dev python3-dev python3-pip virtualenvwrapper htop

export WORKON_HOME=$HOME/.virtualenvs
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh

echo "" >> ~/.bashrc
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "source /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> ~/.bashrc


mkvirtualenv -a /opt/ppp -p /usr/bin/python3 ppp
pip install -r requirements.txt
pip install -e .
