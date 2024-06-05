# Consult Evaluation

> [!IMPORTANT]
> Incubation Project: Consult is an incubation project; as such, we don't recommend using it for critical use cases yet. We are currently in a research stage, trialling the tool for case studies across the Civil Service.


## About this project
This is the evaluation for Consult - our product to analyse government consultations using AI. More information on the project here: https://ai.gov.uk/projects/consultations/. The repository for the tool is here: https://github.com/i-dot-ai/consultation-analyser/.

Detailed docs including evaluation approach can be found in `docs/`.


## Setup

This project uses:
- `poetry` for dependency managagement (https://python-poetry.org/)
- `precommit` to check commits to avoid committing sensitive data (https://pre-commit.com/)
- `ruff` for linting and formatting (https://docs.astral.sh/ruff/)
- `mypy` for checking type hints (https://mypy.readthedocs.io/en/stable/)

Make sure you have Python 3.12, `poetry` and `precommit` installed on your laptop. Then run `poetry install` to install relevenat packages.

For linting and formatting: `make check-python-code` and `make format-python-code`. See the `Makefile` for more details (`make help`).


## Data & outputs

Do **NOT** commit any data to this repo. Store all data in a `data/` folder (should be in `.gitignore` but do check). 

There is a pre-commit tool to strip out any data from a Jupyter Notebook - be warned!

Similarly, store outputs in a folder that is not committed (add details to README at this stage).


## Environment variables

Copy the `.env.example` template file and rename it `.env`. This is where you can add your local environment variables - do not commit this file (it is in the `.gitignore`).


## How to run the code

TBC


## Running tests
Tests use `pytest` - run `make test` to run all of them.

