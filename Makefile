# Project configuration
PROJECT_NAME = commsys_backend_server
PYTHON := python
VENV_NAME := venv
PIP:=pip
WD=$(shell pwd)
PYTHONPATH=${WD}

# Targets

# create virtual environemnt
create-venv:
	@echo "Creating virtual environment..."
	@$(PYTHON) -m venv $(VENV_NAME)
	@echo "Virtual environment created."


# execute_in_env target is a generic macro to run commands within the virtual environment
# Note: It's not a typical target that will be executed directly, but rather a utility for other targets.
.PHONY: execute_in_env

# Define the execute_in_env macro to activate the virtual environment and run a specified command
ACTIVATE_ENV := source venv/bin/activate

define execute_in_env
    $(ACTIVATE_ENV) && $1
endef


# Common Commands
## print requirements
print-req:
	$(call execute_in_env, pip freeze > requirements.txt)

##install requirements 
install-req:
	$(call execute_in_env, pip install -r requirements.txt)

## Run a single test
unit-test:
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH} pytest -v ${test_run})

## Run all the unit tests
test-all:
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH} pytest -v)


## run app 
run-app:
	$(call execute_in_env, Flask run --debug -p 4999)

# run flake8
run-flake:
	$(call execute_in_env, flake8 \
	./app/*.py \
	./app/model/*.py \
	./app/db/*.py \
	./app/controller/*.py \
	./app/blueprint/*.py \
	./test/unit_test/*.py)

## set-up database
setup-db:
	$(call execute_in_env, psql -f ./db/db-setup.sql)
## Run all checks
run-checks: test-all run-flake