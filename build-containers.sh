#!/bin/bash

if [ $# -eq 0 ] ; then
    echo ""
    echo ">>> Please input the enviroment you want to build <<<"
    echo ">>>           production, dev, homolog            <<<"
    echo ""
    exit 1
fi


for d in services/*; do
    (
        # Getting folder name
        name="${d%"${d##*[!/]}"}"
        name="${name##*/}";

        # Building Container
        echo "Building $name:$1: "
        cd "$d"
        docker build -t farmacia-solidaria/$name:$1 .
        docker tag farmacia-solidaria/$name:$1 farmacia-solidaria/$name:latest
    );
done