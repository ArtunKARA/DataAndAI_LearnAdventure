#!/usr/bin/env python3

import sys
import json

output_file = open("map_output.txt", "w")

for line in sys.stdin:

    data = json.loads(line)
    category = data["category"]  
    headline = data["headline"]
    
    words = headline.lower().split()
    
    for word in words:
        output_line = f'{word}\t{category}'
        print(output_line)
        output_file.write(output_line + "\n")

output_file.close()
