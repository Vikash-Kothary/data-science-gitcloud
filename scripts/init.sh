#!/bin/bash
# file: init.sh

if [[ "${ENV}"=="local" ]]; then
	poetry install
else
	echo 'TODO'
	exit 1
fi