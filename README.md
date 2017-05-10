# Python Parallel Processing Presentation

Notes and Code for a presentation to the DAES CG.

## EC2 user-data to set up instances
```sh
#!/bin/bash

pushd /opt
sudo git clone https://github.com/kotfic/ppp.git
sudo chown -R ubuntu:ubuntu ppp
pushd ppp
sudo -u ubuntu ./bootstrap_ec2.sh
```
