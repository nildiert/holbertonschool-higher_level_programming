#!/usr/bin/env bash
# Command to display the size of the content in a headr
curl -Is $1 | grep Content-Length | cut -d" " -f2
