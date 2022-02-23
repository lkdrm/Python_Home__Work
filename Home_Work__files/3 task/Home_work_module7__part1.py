#3 task:
# You have a text file. Write its lines to another file. The order
# of lines in the second file must be inverse.

with open("third_text.txt","r") as reader,open("reverse_third_task.txt","w") as output:
    read = reader.readlines()
    read.reverse()
    output.writelines(read)

