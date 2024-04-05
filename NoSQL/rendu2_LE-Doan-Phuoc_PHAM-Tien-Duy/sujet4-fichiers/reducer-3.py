#!/usr/bin/env python3
import sys

current_user = None
current_count = 0

for line in sys.stdin:
    line = line.strip()

    # Parse the input from mapper.py
    user, count = line.split('\t')

    try:
        count = int(count)
    except ValueError:
        # Ignore/discard this line if count wasn't a number
        continue

    if current_user == user:
        current_count += count
    else:
        if current_user is not None:
            # Write the previous user's count to STDOUT
            print(f'{current_user}\t{current_count}')
        current_user = user
        current_count = count

if current_user is not None:
    print(f'{current_user}\t{current_count}')
