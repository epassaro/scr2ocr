#!/usr/bin/env bash

set -e

echo
conda-lock lock -p linux-64 -p win-64

echo
conda-lock render conda-lock.yml

exit 0
