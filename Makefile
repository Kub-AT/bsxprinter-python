init:
	pip install -r requirements.txt

test:
	nosetests --with-coverage --cover-erase --cover-package=bsxprinter tests.py

.PHONY: init test