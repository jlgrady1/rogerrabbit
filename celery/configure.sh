#!/bin/bash

# root vars
export WORKERHOME=/home/worker
export KIIPHOME=$WORKERHOME/kiip

# Create user
adduser --disabled-password --gecos '' worker
adduser worker sudo
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
