#!/bin/bash

(crontab -l 2>/dev/null; echo "0,30 8-20 * * * /usr/local/bin/armadillo $1 $2 $3") | crontab -
