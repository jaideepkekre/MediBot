#!/usr/bin/env bash

#Owner :Jaideep Kekre
#_author_ = Jaideep Kekre
#_info_   = This module contains a Bash script

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH=":$DIR/bin:$PYTHONPATH:"
export PYTHONPATH=":$DIR/expert_system:$PYTHONPATH"
export PYTHONPATH=":$DIR/lib:$PYTHONPATH"
export PYTHONPATH=":$DIR/data:$PYTHONPATH"

python $DIR/bin/server.py
