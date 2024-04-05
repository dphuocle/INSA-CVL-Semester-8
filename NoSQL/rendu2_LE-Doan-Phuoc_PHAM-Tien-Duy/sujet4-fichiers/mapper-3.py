#!/usr/bin/env python3
import sys

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove any leading and trailing spaces
    line = line.strip()

    # Split the line into 'followed' and 'follower'
    followed, follower = line.split(',')

    # Emit the 'followed' user as the key and '1' as the value
    print(f'{followed}\t1')
