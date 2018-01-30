#!/bin/bash
echo "Delete old enviorement_________"
rm -rf virtualenv
echo "Install virtualenv_____________"
pip install virtualenv
echo "Create environment_____________"
#virtualenv -p python3 virtualenv
virtualenv -p python3 virtualenv
echo "Start environment______________"
source virtualenv/bin/activate
echo "Install requirements.apt_______"
sudo apt-get install $(cat requirements.apt)
echo "Install requirements.txt_______"
pip install -r requirements.txt
echo "[Finish]"
