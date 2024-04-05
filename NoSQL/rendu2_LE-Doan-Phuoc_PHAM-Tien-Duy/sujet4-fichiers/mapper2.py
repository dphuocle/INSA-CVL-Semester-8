#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    entry = line.split(',')
    key = entry[0]
    value = line[1:]
    if key == 'M':
        print('{0}\t{1}'.format(key,value))
    elif key == 'N':
        print('{0}\t{1}'.format(key,value))


