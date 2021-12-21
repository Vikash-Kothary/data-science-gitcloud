#!/usr/bin/env bash
# file: poetry-export.sh
# description:
# description: Lock dependencies and export requirements.

# Export requirements.txt
echo -e "# THE FILE WAS GENERATED BY POETRY, DO NOT EDIT!\n\n" > src/requirements.txt
echo -e "# THE FILE WAS GENERATED BY POETRY, DO NOT EDIT!\n\n" > src/requirements-dev.txt
poetry lock
poetry export --without-hashes -f requirements.txt >> src/requirements.txt
poetry export --dev --without-hashes -f requirements.txt >> src/requirements-dev.txt

echo "-e src/." >> src/requirements-dev.txt
