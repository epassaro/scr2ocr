#!/usr/bin/env bash

set -e

echo
conda-lock lock -f environment.yml

echo
conda-lock render conda-lock.yml

exit 0
