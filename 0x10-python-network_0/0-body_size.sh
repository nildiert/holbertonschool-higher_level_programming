#!/bin/bash
# Command to display the size of the content in a headr
curl -sI $1 | grep Content-Length | cut -d" " -f2
