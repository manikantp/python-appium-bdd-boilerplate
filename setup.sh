#!/usr/bin/env bash

rm -rf venv
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
#deactivate