#!/bin/sh
PWD=`pwd`

# create a virtual environment in the project
python3 -m venv ./venv


activate () {
    echo $PWD
    source $PWD/venv/bin/activate
}

activate

# install dependencies
pip install -r ./requirements.txt