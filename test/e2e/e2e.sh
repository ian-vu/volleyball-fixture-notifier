#!/usr/bin/env bash

STAGE=$1
if [[ -z $STAGE ]]
  then echo "STAGE expected as first positional argument. STAGE not found.";
  exit 1;
fi

# Invoke function and expect log line to contain string
sls invoke --function cronHandler --stage $STAGE --log | grep "Successfully published message to email."