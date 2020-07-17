#/bin/make

SHELL := /bin/bash
GIT_PORTFOLIO_NAME ?= "Git Portfolio"
GIT_PORTFOLIO_VERSION ?= "v0.1.0"
GIT_PORTFOLIO_DESCRIPTION ?= "Manage all your Git repositories, organisations, providers from one place."
ENV ?= local

include config/.env.${ENV}
export

.DEFAULT_GOAL := help
.PHONY: help #: Display this self documenting help dialog
help:
	@awk 'BEGIN {FS = " ?#?: "; print ""$(GIT_PORTFOLIO_NAME)" "$(GIT_PORTFOLIO_VERSION)"\n"$(GIT_PORTFOLIO_DESCRIPTION)"\n\nUsage: make \033[36m<command>\033[0m\n\nCommands:"} /^.PHONY: ?[a-zA-Z_-]/ { printf "  \033[36m%-10s\033[0m %s\n", $$2, $$3 }' $(MAKEFILE_LIST)

.PHONY: init
init:
	@$(OPEN) http://localhost:8080
	@$(MKDOCS) serve -f docs/mkdocs.yml

.PHONY: docs
docs:
	@$(OPEN) http://localhost:8080
	@$(MKDOCS) serve -f docs/mkdocs.yml

.PHONY: notebooks #: Run Jupyter notebooks
notebooks:
	@$(JUPYTER) lab

.PHONY: lint
lint:
	@$(OPEN) reports/index.html
	@$(FLAKE8) --format=html --htmldir=reports src tests

.PHONY: tests
tests:
	@$(PYTEST) tests

.PHONY: run
run:
	@$(OPEN) http://localhost:5000
	@$(FLASK) run

.PHONY: clean #: Delete build files.
clean:
	@[[ -z "${FORCE}" ]] || rm -r .venv
	@find . -name .ipynb_checkpoints -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name __pycache__ -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name *.pytest_cache -type d -not -path .venv -print0 | xargs -0 rm -r
	@find . -name *.egg-info -type d -not -path .venv -print0 | xargs -0 rm -r

%:
	@sh scripts/$(*).sh