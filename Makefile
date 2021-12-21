#!/usr/bin/env make

DATA_SCIENCE_GITCLOUD_ID ?= 20015553
DATA_SCIENCE_GITCLOUD_NAME ?= data-science-gitcloud
DATA_SCIENCE_GITCLOUD_VERSION ?= v0.1.0
DATA_SCIENCE_GITCLOUD_DESCRIPTION ?= Manage all your Git repositories, organisations, providers from one place.

ENV ?= local
-include config/.env.${ENV}
-include config/secrets/.env.*.${ENV}
export

.DEFAULT_GOAL := help
.PHONY: help #: List available commands.
help:
	@${AWK} 'BEGIN {FS = " ?#?: "; print "$(DATA_SCIENCE_GITCLOUD_NAME) $(DATA_SCIENCE_GITCLOUD_VERSION)\n$(DATA_SCIENCE_GITCLOUD_DESCRIPTION)\n\nUsage: make \033[36m<command>\033[0m\n\nCommands:"} /^.PHONY: ?[a-zA-Z_-]/ { printf "  \033[36m%-10s\033[0m %s\n", $$2, $$3 }' $(MAKEFILE_LIST)

.PHONY: docs #: Run documentation.
docs:
	@${MKDOCS} ${MKDOCS_OPTS} -f docs/mkdocs.yml

.PHONY: lint #: Run linting.
lint:
	@${PRECOMMIT} run --all-files
# 	@$(FLAKE8) --format=html --htmldir=reports src tests

.PHONY: tests #: Run tests.
tests:
	@${PYTEST} --doctest-modules tests/

.PHONY: run #: Run application.
run: 
	@${UVICORN} gitcloud_app.main:app --reload

# Run scripts using make
%:
	@if [[ -f "scripts/${*}.sh" ]]; then \
	${BASH} "scripts/${*}.sh" ${LOGGER}; fi

.PHONY: init #: Download project dependencies.
init:
	@${POETRY} install

.PHONY: config #: Create environment-specific config files.
config: config/.env.${ENV}
config/.env.%:
	@cp -n config/.env.example config/.env.${ENV}

.PHONY: open #: Open application in the browser.
open:
	@${OPEN} ${DATA_SCIENCE_GITCLOUD_URL}

.PHONY: clean #: Clean project build files.
clean:
	@[[ -z "${FORCE}" ]] || rm -r .venv
	@find . -name .ipynb_checkpoints -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name __pycache__ -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name *.pytest_cache -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name *.egg-info -type d -not -path .venv -print0 | xargs -0 rm -r
