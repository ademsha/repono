#!/bin/bash
# Push to Git Repo

source $HOME/.keychain/$(hostname)-sh

# Example: APP_DIR="/home/YOUR-USERNAME/repono/"
APP_DIR=""
# Location of your virtualenv python version or just PYTHON_DIR="python" for system-wide level
PYTHON_DIR=""

echo "Export of compressed files started // " $(date -u)

cd $APP_DIR"data/files/compressed/"

# Push to Git Repo
commit_message="Automatic backup of collected datasets // $(date -u)"
git add . -A
git commit -m "$commit_message"
git push

echo "Export of of compressed files finished // " $(date -u)