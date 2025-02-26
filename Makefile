.PHONY: install run

install:
	poetry install

run:
	poetry run python ./karma_farmer/main.py
