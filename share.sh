#!/bin/bash
SCRIPT_PATH=$(realpath "${BASH_SOURCE[0]}")
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
echo "Absolute script directory: $SCRIPT_DIR"
python -m pip install -r requirements.txt

PORT=8000

# change the share directory to your desired location
SHARE_DIR=~/

cd $SHARE_DIR
python3 $SCRIPT_DIR/share.py $PORT
