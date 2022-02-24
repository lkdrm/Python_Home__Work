# 9 task:
# You have a text file. Calculate the number of characters in it.

import re

with open("nineth_text.txt","r") as reader:
    sum_of_leters = []
    for word in reader:
        sum_of_leters.append(len(word))
    print(r"The sum of letters are:",sum(sum_of_leters))