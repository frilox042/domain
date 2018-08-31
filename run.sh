#!/bin/bash

python -m mypy *.py
python -m pylint *.py
python -m unittest *.py

python main.py