#1 First task:
#The user types in two numbers. Print all the numbers in
#the specified range:
"""
print("Hello the program will created a range.\nBut first you need to write the value from start to end of range")
a = int(input("Enter the first numb of range:"))
b = int(input("Enter the last numb of range:"))

for i in range(a,b+1):
    print(i)
print("End of program")
"""

#2 Second task:
# The user types in two numbers. Print all even numbers in
# the specified range:
"""
print("Hello the program will created the range only of odd numbers")
a = int(input("First number of range:"))
b = int(input("Last number of range:"))

for i in range(a,b+1):
    if i%2==0:
        print(i)

print("End of program")
"""

#3 Third task:
#The user types in two numbers. Print all odd numbers in
#the specified range:
"""
print("Hello the program will created the range only of even numbers")
a = int(input("Enter the first numb of range:"))
b = int(input("Enter the last numb of range:"))

for i in range(a,b+1):
    if i%2 !=0:
        print(i)
print("End of program")
"""

#4 Fourth task:
#The user types in two numbers. Print all numbers in the
#specified range in descending order:
"""
print("Hello the program will created the range but in descending order")

a = int(input("Enter the first numb of range, but must be bigger as last, because won`t work:"))
b = int(input("Enter the last number of range:"))

for i in range(a,b-1,-1):
    print(i)
print("End of program")
"""
#5 Fifth task:
# The user types in two numbers. Print all odd numbers in
# the specified range. If the end and start points of the range
# are incorrect, normalize them. Let’s say the user typed in 33
# and 13, normalization will assign 13 to the start and 33 to the
# end of the range:
"""
a = int(input("Enter the start value of range:"))
b = int(input("Enter the last value of range:"))

if b > a :
    print("First")
    for i in range (a,b+1):
        if i%2 !=0:
            print(i)
elif a > b:
    print("You just write, incorrect we have change to write form:")
    for i in range (b,a+1):
        if i%2 !=0:
            print(i)
else:
    print("Please, enter the valid numbers")

print("End of program")
"""