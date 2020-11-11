#!/bin/bash
python3 manage.py dumpdata --natural-primary --natural-foreign --indent=4 --exclude=contenttypes > rameniaapp/fixtures/dbseed.json