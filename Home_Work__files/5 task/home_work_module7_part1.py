#5 task:
# You have a text file. Calculate the number of words that
# begin with a character set by the user.

with open("fifth_text.txt","r") as reader:
    sum_of_leters = []
    for word in reader:
        sum_of_leters.append(len(word))
    print(r"The sum of letters are:",sum(sum_of_leters))