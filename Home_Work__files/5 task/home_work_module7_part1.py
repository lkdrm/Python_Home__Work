#5 task:
# You have a text file. Calculate the number of words that
# begin with a character set by the user.

import re
"""
with open("fifth_text.txt","r") as reader:
    sum_of_leters = []
    for word in reader:
        sum_of_leters.append(len(word))
    print(r"The sum of letters are:",sum(sum_of_leters))
"""
letter = input("Enter which letter we are looking for")
regex_compile = re.compile(r"[d]")
# i can use (fr"{letter}")
with open ("fifth_text.txt", "r") as reader:
    sum_of_leters = []
    for letter in reader:
        regex_search = regex_compile.findall(letter)
        if len(regex_search) > 0 :
            #print(regex_search)
            for index in regex_search:
                sum_of_leters.append(index)
    print("The sum of my letters are:",len(sum_of_leters))
