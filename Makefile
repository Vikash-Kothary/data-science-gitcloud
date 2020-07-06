#/bin/make

SHELL := /bin/bash
GIT_PORTFOLIO_NAME ?= "Git Portfolio"
GIT_PORTFOLIO_VERSION ?= "v0.1.0"
GIT_PORTFOLIO_DESCRIPTION ?= "Manage all your Git repositories, organisations, providers from one place."
-include .env
export

.DEFAULT_GOAL := help
.PHONY: help #: Display this self documenting help dialog
help:
	@awk 'BEGIN {FS = " ?#?: "; print ""$(GIT_PORTFOLIO_NAME)" "$(GIT_PORTFOLIO_VERSION)"\n"$(GIT_PORTFOLIO_DESCRIPTION)"\n\nUsage: make \033[36m<command>\033[0m\n\nCommands:"} /^.PHONY: ?[a-zA-Z_-]/ { printf "  \033[36m%-10s\033[0m %s\n", $$2, $$3 }' $(MAKEFILE_LIST)

.PHONY: init #: Initiase environment
init:
	@poetry install

.PHONY: lint
lint:
	@[[ -d .venv ]] || ${MAKE} init
	@poetry run flake8 src tests

.PHONY: notebooks #: Run Jupyter notebooks
notebooks:
	@[[ -d .venv ]] || ${MAKE} init
	@poetry run jupyter lab

.PHONY: tests
tests:
	@[[ -d .venv ]] || ${MAKE} init
	@poetry run pytest tests

.PHONY: build
build:
	@poetry build

.PHONY: release
release:
	@poetry publish

.PHONY: run
run:
	@[[ -d .venv ]] || ${MAKE} init
	@flask run

.PHONY: clean #: Delete build files.
clean:
	@[[ -z "${FORCE}" ]] || rm -r .venv
	@find . -name .ipynb_checkpoints -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name __pycache__ -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name *.pytest_cache -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name *.egg-info -type d -not -path .venv -print0 | xargs -0 rm -r
