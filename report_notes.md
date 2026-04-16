name: Working CI Pipeline

on:
  push:
    branches:
      - develop
  pull_request:
    branches:
      - main

jobs:
  test-and-lint:
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run lint gate
        run: flake8 cart.py tests

      - name: Run full test suite
        run: python -m unittest discover -s tests -v
