#!/usr/bin/bash

mkdir /tmp/Run_localtunnel
cd /tmp/Run_localtunnel

npm install -g localtunnel
nohup lt --port $1 > /content/IDE_on_Colab/localtunnel.log 2>&1 &
sleep 10
