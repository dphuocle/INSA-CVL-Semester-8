#!/usr/bin/env python3
import sys
import re

# This function will tokenize lines into words and remove punctuation.
def tokenize(text):
    # Replace punctuation with space, convert to lowercase, and split into words
    return re.sub(r"[^\w\s]", " ", text.lower()).split()

for line in sys.stdin:
    for word in tokenize(line):
        print(f"{word}\t1")
