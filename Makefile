.PHONY: default style test run

FILENAME?=test.jt

default:
	@echo "valid commands are:"
	@echo "  style - run pycodestyle against .py files"
	@echo "  test - run unit tests"

style:
	@echo "Checking style on .py files"
	./.env/bin/pycodestyle bin/jtracker
	./.env/bin/pycodestyle libjtracker/*

test:
	python -m unittest discover test

run:
	./.env/bin/jtracker $(FILENAME)