#2 task:
# Task 2
# You have a text file. Write its lines to another file. The
# order of lines in the second file must match the order of lines
# in the source file.

with open("Second_text.txt","r") as reader, open("Second_text__ready.txt","w") as outside:
    outside.writelines(reader)
