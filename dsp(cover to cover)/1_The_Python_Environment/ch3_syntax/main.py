#!/usr/bin/env python3.10
import sys
print(sys.version) # 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
## because venv was intialized with pyhthon3.10 -m venv/env
print(sys.argv) #  ['./main.py']
## script name and additional arguments thereafter are turned into a list of strings and assigned to the argv variable in the sys module