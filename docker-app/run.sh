#!/bin/bash

echo 'Starting CherryPy HTTP server..'
/serve.py tech.zalando.com/output/ &

while true; do
    echo 'Cloning git repo..'
    git clone https://github.com/zalando/tech.zalando.com.git
    (
    cd tech.zalando.com
    echo 'Pulling git repo..'
    git pull
    rm -fr .doit*
    echo 'Building static HTML with Nikola..'
    nikola build
    )
    echo 'Sleeping 45s..'
    sleep 45
done
