#!/usr/bin/env python3
import sys
from itertools import groupby
from operator import itemgetter

# This function reads input from stdin and groups lines by each unique word.
def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

data = read_mapper_output(sys.stdin)
for current_word, group in groupby(data, itemgetter(0)):
    total_count = sum(int(count) for current_word, count in group)
    print(f"{current_word}\t{total_count}")
