#!/bin/bash

set -xe

chmod 600 ~/.ssh/id_rsa
ssh-keyscan -H "${{ secrets.EC2_INSTANCE_IP }"} >> ~/.ssh/known_hosts
ssh -i  ~/.ssh/id_rsa ubuntu@"${{ secrets.EC2_INSTANCE_IP }"}

