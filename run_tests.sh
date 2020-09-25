#!/bin/sh
echo '************'
echo  flake8
echo '************'
flake8
X_flake8=$?
echo

echo '************'
echo  mypy
echo '************'
mypy --ignore-missing-imports nano_editorconfig nec
X_mypy=$?
echo

echo '************'
echo  pytest
echo '************'
pytest
X_pytest=$?

(exit $X_flake8) && (exit $X_mypy) && (exit $X_pytest)
