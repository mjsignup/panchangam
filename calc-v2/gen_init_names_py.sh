#!/bin/bash
echo init_names.txt `ls *_names.txt | grep -v init` | xargs cat > init_names.py
