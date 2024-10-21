#!/usr/bin/env python3

import sys
from collections import defaultdict

output_file = open("reduce_output.txt", "w")

current_word = None
category_list = defaultdict(int)

for line in sys.stdin:
    word, category = line.strip().split("\t")
    
   
    if current_word == word:
        category_list[category] += 1  
    else:
        if current_word:
            # Önceki kelime için sonuçları yazdır
            output_line = f'{current_word}\t{list(category_list.items())}'
            print(output_line)  
            output_file.write(output_line + "\n") 
        current_word = word
        category_list = defaultdict(int)
        category_list[category] = 1

if current_word == word:
    output_line = f'{current_word}\t{list(category_list.items())}'
    print(output_line) 
    output_file.write(output_line + "\n")  

output_file.close()