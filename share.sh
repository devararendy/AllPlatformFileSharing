#!/bin/bash
SCRIPT_PATH=$(realpath "${BASH_SOURCE[0]}")
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
echo "Absolute script directory: $SCRIPT_DIR"

PORT=8000

cd ~/storage/dcim/sharing
python3 $SCRIPT_DIR/share.py $PORT
