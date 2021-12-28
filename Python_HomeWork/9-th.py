#1 First task:
# The user types in two numbers (start and end points of
# the range). Analyze all the numbers in this range as follows:
# if the number is a multiple of 7, print it:
"""
print("Hello the programm will find all numbers which are multiples of 7, from start of range to end ")
a = int(input("Enter the start of range:"))
b = int(input("Enter the end of range:"))

for i in range(a,b+1):
    if i%7==0:
        print("This numbers are multiple of 7:",i)

print("End of programm")
"""
#2 Second task:
# The user types in two numbers (start and end points
# of the range). Analyze all the numbers in this range. Print
# the following:
# 1. All numbers in the range;
# 2. All numbers in the range in descending order;
# 3. All numbers that are multiples of 7;
# 4. How many numbers are multiples of 5.
print("Hello this programm will analyze all the numbers in this range")
print("And print the following:",
      "1. All numbers in the range;",
      "2. All numbers that are multiples of 7;",
      "3. How many numbers are multiples of 5;",
      "4. All numbers in the range in descending order.",
      sep="\n")
a = int(input("Enter the start of range:"))
b = int(input("Enter the end of range:"))

count = 0

for i in range(a,b+1):
    print(i)
    if i%7==0:
        print("The numbs are multiples of 7:",i)
    if i%5==0:
        print("The numbs are multiples of 5:",i)
        count+=1

print("All counts is:", count)

for i in range(b,a,-1):
    print(i, end=" ")

print("Enf of programm")
