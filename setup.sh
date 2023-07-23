#!/bin/bash

set -xe

sudo apt update
sudo apt-install unzip
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

sudo apt install docker.io
sudo systemctl start docker
sudo usermod -aG docker "$USER"