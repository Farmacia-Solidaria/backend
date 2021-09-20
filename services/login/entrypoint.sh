#!/bin/bash

python createAndConfigure.py

(service-django runserver) &
(service-faust worker -l info) 