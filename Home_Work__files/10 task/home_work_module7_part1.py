# 10 task:
# You have a text file. Calculate the number of lines in it.

with open ("tenth_text.txt","r") as reader:
    lines = reader.readlines()
    print("The numberes of lines is text are:",len(lines))