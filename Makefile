# Python Project Makefile
# Authors: Aqeel Akber <aqeel.akber@gmail.com>
#
# This is predominately used to ease / speed up development.

env:
	virtualenv env
	@echo "------------------------------------------------------------------------"
	@echo "FINISHED INITIALISING PYTHON VIRTUAL ENVIRONMENT"
	@echo 
	@echo "To use it, run:"
	@echo 
	@echo ". env/bin/activate"
	@echo "## Optionally, make IPython use right env"
	@echo "alias ipy=\"python -c 'import IPython; IPython.terminal.ipapp.launch_new_instance()'\""
	@echo 
	@echo "When finished, run:"
	@echo 
	@echo "deactivate"
	@echo "unalias ipy # optional"
	@echo "------------------------------------------------------------------------"

getreqs:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements_freeze.txt

test:
	pytest tests

.PHONY:
	env getreqs freeze test
