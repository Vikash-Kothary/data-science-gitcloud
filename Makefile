#/bin/make
#@ Git Migration

GIT_MIGRATION_NAME ?= "Git Migration"
GIT_MIGRATION_VERSION ?= "v0.1.0"
GIT_MIGRATION_DESCRIPTION ?= "Move git repositories between git providers."
GIT_MIGRATION_ROOT ?= $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

-include .env
export

.DEFAULT_GOAL := help
.PHONY: help #: Display this self documenting help dialog
help:
	@cd ${GIT_MIGRATION_ROOT} && awk 'BEGIN {FS = "\.PHONY:.*##"; print ""${GIT_MIGRATION_NAME}" "${GIT_MIGRATION_VERSION}"\n"${GIT_MIGRATION_DESCRIPTION}"\n\nUsage: make \033[36m<command>\033[0m\n\nCommands:"} /^[a-zA-Z_-]+:.*?/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: init #: Initiase environment
init:
	@cd ${GIT_MIGRATION_ROOT} && \
	[[ -f .env ]] || cp .env.example .env && \
	[[ -d .venv ]] || poetry install

.PHONY: notebooks #: Run Jupyter notebooks
notebooks: init
	@poetry run jupyter notebook --notebook-dir=./notebooks