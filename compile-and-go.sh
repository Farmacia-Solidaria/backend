#!/bin/bash

python3 safeBuild.py --env dev --containers all --update-commons
docker-compose up --build --remove-orphans