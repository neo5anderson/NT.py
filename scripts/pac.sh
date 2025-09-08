#!env bash

# --hidden-import=matplotlib \
# --hidden-import=openpyxl \
# --hidden-import=pandas \
# --hidden-import=scikit-learn \
# --hidden-import=sympy \

rm -rf dist/*

uv run pyinstaller --clean \
  -F ./src/nt25/lib/et.py
