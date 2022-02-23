"""
import os

files = open("First_task.txt","w")
files.write("Hello, how do you do?\n")
files.write("Thank i`m fine. \n")
files.write("The longestword which i`m must to find.\n")

files.close()

"""

#1 First task:
# You have a text file. Create a new file where you should
# write all words consisting of at least seven letters found in the
# source file.

import re

with open("First_task.txt","r") as reader, open("First_task__ready.txt","w") as output:
    for word in reader:
        regex_compile = re.compile(r"\w{7,}")
        regex_search = regex_compile.findall(word)
        words = " ".join(regex_search)
        output.write(words)
        output.write("\n")




#######better version:
import re
regex_compile = re.compile(r"\w{7,}")

with open("First_task.txt","r") as reader, open("First_task__ready.txt","w") as output:
    for line in reader:
        regex_search = regex_compile.findall(line)
        if len(regex_search) > 0:
            words = " ".join(regex_search)
            output.write(words)
            output.write("\n")

