#!/bin/bash
# Curl json File
curl -sd "@$2" -H "Content-Type: application/json" -X POST "$1"
