#!/bin/bash
read -rp "Enter your username (0000xx/000xxx): " USERNAME
read -srp "Enter your password (Default ID number): " PASSWORD

sed -i -e "s/__USERNAME__/${USERNAME}/" main.py
sed -i -e "s/__PASSWORD__/${PASSWORD}/" main.py

# Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv env
# Activate the virtual environment
source env/bin/activate
# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt
# Leave the virtual environment
deactivate