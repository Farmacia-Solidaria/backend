#!/bin/bash

python createAndConfigure.py

python manage.py runserver & python kafka_handler/app.py worker