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

.PHONY: notebooks #: Run Jupyter notebooks
notebooks: init
	@poetry run jupyter notebook --notebook-dir=./notebooks

.PHONY: run
run:
	@flask run