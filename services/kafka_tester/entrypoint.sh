#!/bin/bash

python createAndConfigure.py

(python manage.py runserver) &
(python modules/kafka_handler/app.py worker)