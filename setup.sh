#!/usr/bin/env bash

rm -rf boilerenv
python3 -m virtualenv boilerenv
source boilerenv/bin/activate
pip3 install -r requirements.txt
#deactivate
