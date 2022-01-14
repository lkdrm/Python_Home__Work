# Task 1:
# The user types in an arithmetic expression. For example,
# 23+12.
# Print its result. In our example, the output is 35. The arithmetic
# expression can have only three parts: number, operation,
# number. Possible operations: +, -, *, /. :
"""
print("Enter a number & value.",
    "Possible operations: +, -, *, /.",
    "You must write like that:","2 + 2 = correct",
    "2+2 = doesn't work",
    sep ="\n")
while True:
    user = input("Write here:")
    change = user.split(" ")
    a,b,c = change
    if b == "+":
        print("The result is:",int(a) + int(c))
    elif b == "-":
        print("The result is:",int(a) - int(c))
    elif b == "*":
        print("The result is:",int(a) * int(c))
    elif b == "/":
        print("The result is:",int(a) / int(c))
    else:
        print("Enter a correct operations")
"""
# Task 2
# You have a list of integers filled with random numbers.
# Find the largest and the smallest elements, count negative and
# positive elements, as well as zeros. Print the results.
"""
import random

i=0
list_of_rand_numbers = []
while i <=5: # Do the iterations 5 times 
    number = random.randint(-99,99) # create a random number
    list_of_rand_numbers.append(number) # send to list
    i+=1    
print(list_of_rand_numbers)

def result(list_of_value):
    positive = []
    negative = []
    for i in list_of_value:
        if i > 0:
            positive.append(i)
        elif i< 0:
            negative.append(i)
    print("The max is:",max(list_of_value))
    print("The min is:",min(list_of_value))
    print("The sum of positive numbers:",sum(positive))
    print("The sum of negative:",sum(negative))
    
result(list_of_rand_numbers)
"""