#!/usr/bin/bash
# Command to display the size of the content in a headr
curl -Is 127.0.0.1 | grep Content-Length | cut -d" " -f2
