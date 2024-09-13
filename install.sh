#/bin/sh

python3 setup.py clean;

python3 setup.py build;

echo 'running installing'
python3 -m pip install --user .
# the above line auto-detects setup.py
