#!/bin/sh
# create a virtual environment in the project
python3 -m venv ./venv


activate () {
    source ./venv/bin/activate
}
# activate the virtual environment to install deps
activate

# install dependencies
pip install -r ./requirements.txt