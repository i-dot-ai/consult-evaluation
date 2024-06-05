# Consult Evaluation

## About this project
This is the evaluation for Consult - 


## Setup

This project uses:
- `poetry` for dependency managagement (https://python-poetry.org/)
- `precommit` to check commits to avoid committing sensitive data (https://pre-commit.com/)
- `ruff` for linting and formatting (https://docs.astral.sh/ruff/)
- `mypy` for checking type hints (https://mypy.readthedocs.io/en/stable/)

Make sure you have Python 3.12, `poetry` and `precommit` installed on your laptop. Then run `poetry install` to install relevenat packages.

For linting and formatting: `make check-python-code` and `make format-python-code`. See the `Makefile` for more details (`make help`).


## Data

Do **NOT** commit any data to this repo. Store all data in a `data/` folder. 


## Environment variables

Copy the `.env.example` template file and rename it `.env`. This is where you can add your local environment variables - do not commit this file (it is in the `.gitignore`).


## How to run the code

TBC


## Running tests
Tests use `pytest` - run `make test` to run all of them.

