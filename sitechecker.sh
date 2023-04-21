#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
date
PYTHONPATH=$SCRIPT_DIR python3 -m sitechecker -f $SCRIPT_DIR/cron_urls.csv
