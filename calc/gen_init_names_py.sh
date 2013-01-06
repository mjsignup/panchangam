#!/bin/bash
mv -v init_names.py init_names.py.$$
echo init_names.txt `ls *_names.txt | grep -v init` | xargs cat > init_names.py
