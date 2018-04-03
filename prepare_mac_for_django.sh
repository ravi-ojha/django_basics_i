#!/usr/bin/env bash

VENV_NAME="k_venv"

# Install pip - Python package manager
sudo easy_install pip
# Install virtualenv
sudo pip install virtualenv
# Create a new virtual env with python2.
# If your python is pointing to Python 2.7 then use `python` instead of `python2`
virtualenv -p python $VENV_NAME
# Activate the virtual env
source $VENV_NAME/bin/activate
# Install django 1.11 in that virtual env
pip install django==1.11

