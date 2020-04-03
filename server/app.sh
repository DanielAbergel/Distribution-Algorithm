#!/bin/bash

isBuild=$1
password=$2
build='build'

if [ "$isBuild" == "$build" ]; then
    echo "Building server for DEBUG purposes"
    
    echo $password | sudo -S pip3 install virtualenv
    echo Y | sudo -S apt-get install virtualenv
    virtualenv venv --python=python3
    source venv/bin/activate
    echo "-- Install server dependencies --"
    pip install -r requirements.txt
    deactivate
else
    echo "Runing DEBUG Server on 'http://127.0.0.1:5000' "
    echo "-- Activating virtual environment --"
    source venv/bin/activate
    echo "-- Running app.py  --"
    python app.py
fi
