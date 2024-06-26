#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Starting setup.sh script"

# Install dependencies
echo "Installing dependencies"
pip install -r requirements.txt

# Run migrations
echo "Running migrations"
python manage.py makemigrations
python manage.py migrate

# Collect static files
echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Setup completed"
