# Python Parallel Processing Presentation

Notes and Code for a presentation to the DAES CG.

## EC2 user-data to set up instances

### Master
```sh
#!/bin/bash

pushd /opt
sudo git clone https://github.com/kotfic/ppp.git
sudo chown -R ubuntu:ubuntu ppp
pushd ppp
sudo -u ubuntu ./bootstrap_ec2.sh
sudo apt-get install rabbitmq-server
# RabbitMQ
sudo rabbitmq-plugins enable rabbitmq_management
echo "[{rabbit, [{loopback_users, []}]}]." | sudo tee /etc/rabbitmq/rabbitmq.config
sudo systemctl restart rabbitmq-server

# Flower
sudo cp /opt/ppp/misc/flower.service /etc/systemd/system/
sudo chmod 664 /etc/systemd/system/flower.service
sudo systemctl daemon-reload
sudo systemctl start flower
```

### Worker
