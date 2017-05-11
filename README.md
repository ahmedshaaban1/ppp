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

# RabbitMQ
sudo apt-get install rabbitmq-server
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

```sh
#!/bin/bash

pushd /opt
sudo git clone https://github.com/kotfic/ppp.git
sudo chown -R ubuntu:ubuntu ppp
pushd ppp
sudo -u ubuntu ./bootstrap_ec2.sh

# Celery Worker
sudo mkdir /var/log/celery
sudo chown ubuntu:ubuntu /var/log/celery
sudo mkdir /var/run/celery
sudo chown ubuntu:ubuntu /var/run/celery
sudo cp /opt/ppp/misc/celery.service /etc/systemd/system/
sudo chmod 664 /etc/systemd/system/celery.service
sudo systemctl daemon-reload
sudo systemctl start celery
```
