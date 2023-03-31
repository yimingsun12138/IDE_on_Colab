#!/usr/bin/bash

mkdir /tmp/Run_ngrok
cd /tmp/Run_ngrok

curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc > /dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
ngrok config add-authtoken $1
ngrok http $2 --log stdout > /content/IDE_on_Colab/ngrok.log &
sleep 10
