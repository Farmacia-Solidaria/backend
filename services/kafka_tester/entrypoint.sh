#!/bin/bash

python createAndConfigure.py

(start-django runserver) &
(start-faust worker -l info)