#!/bin/bash
# This script is a shortcut to create a fixture from your current DB state
python3 manage.py dumpdata --natural-primary --natural-foreign --indent=4 --exclude=contenttypes > rameniaapp/fixtures/dbseed.json