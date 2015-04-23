#!/usr/bin/env python3

import fileinput
import re

for line in fileinput.input():
    items = line.split('\t')
    if len(items) == 14:
        if items[0] == 'Kirjauspäivä':
            # It's the documentation line, skip
            continue
        for i in items:
            print(i.strip().replace(',', '.'), end=",")
        print()
