#!/bin/bash
pip install pytest-django
pytest --junitxml=test-results/junit.xml /gitRoot/djangodemo/tests
python /gitRoot/djangodemo/setup.py sdist
cp -r -n /gitRoot/ /code/  
cp -r -n /gitRoot/ /code/