#!/bin/bash

while true; do
    cd /workdir
    echo 'Cloning git repo..'
    git clone https://github.com/zalando/tech.zalando.com.git
    (
    cd /workdir/tech.zalando.com
    echo 'Pulling git repo..'
    git pull
    rm -fr .doit*
    echo 'Building static HTML with Nikola..'
    nikola build
    )
    echo 'Sleeping 45s..'
    sleep 45
done
