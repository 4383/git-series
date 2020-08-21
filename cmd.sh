#!/bin/bash
sed -i "s/hacking>=3.0.1,<3.1.0/hacking>=3.2.0,<3.3.0/g" test-requirements.txt
if [ -f .pre-commit-config.yaml ]; then
    sed -i "s/hacking>=3.0.1,<3.1.0/hacking>=3.2.0,<3.3.0/g" .pre-commit-config.yaml;
fi
