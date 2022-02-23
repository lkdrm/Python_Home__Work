#4 task:
# You have a text file. Add a line consisting of twelve asterisks
# (************) after the last line among the lines that have
# no comma. If there are no such lines in the file, the asterisks
# should be added after all lines of the existing file. Write the
# result to another file.

with open("fourth_text.txt","r") as reader, open("text_stars.txt","w") as output:
    stars = False
    for line in reader:
        output.write(line)
        if not line.endswith(",\n") and not stars:
            if not line.endswith("?\n") and not stars:
                if not line.endswith("!\n") and not stars:
                    if not line.endswith(".\n") and not stars:
                        stars = True
                        output.write("************\n") 

