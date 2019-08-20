#!/bin/bash
# Curl json File
curl -d "@$2" -H "Content-Type: application/json" -X POST "$1"
