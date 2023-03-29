#!/usr/bin/bash

# create temp installation path
mkdir /tmp/Install_Rstudio_server
cd /tmp/Install_Rstudio_server

# install
apt install gdebi-core
wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-2023.03.0-386-amd64.deb
gdebi -n rstudio-server-2023.03.0-386-amd64.deb
