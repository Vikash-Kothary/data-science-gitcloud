#!/usr/bin/env bash
# file: jupyter-clean.sh
# description:

find notebooks -name *.ipynb -print0 | xargs -0 nbstripout