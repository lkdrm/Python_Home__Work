#1 First task:
# Write a program that requests two integers x and y, and
# then calculates and prints the value of x raised to the power of y:
"""
print("Hello the programm requests two integers x and y, and then calculates and prints the value of x raised to the power of y.")
x = int(input("Enter x:"))
y = int(input("Enter y:"))

count = x**y

print("The value of x raised to the power of y:")
print("x:",x)
print("y:",y)
print("The count is:",count )

print("End of programm")
"""

#2 Second task:
# Count the number of integers in the range from 100
# to 999 that have two identical digits:
"""
count = 0
count_2 = 0
for i in range(100,999):
        a = i
        b = str(a)
        if b[0] == b[1] and b[1] == b[2]:
                print("All 3 values are same:",b,sep="\n")
                count+=1
        if b[1] == b[2]:
                print("All 2 values are same:",b,sep="\n")
                count_2+=1

print("All numbs which have 3 same values:",count)
print("All numbs which have only 2 same values:",count_2)
print("End of programm")
"""
#3 Third task:
# Count the number of integers in the range from 100
# to 9999 that have different digits:

count = 0

for i in range(100,999):
        a = i
        b = str(a)
        if b[0] != b[1] and b[1] != b[2] and b[2] != b[0]:
                count+=1

print("All values are:",count) 
print("End of programm")

#4 Fourth task:
# The user types in an integer value. Remove all 3s and 6s
# from this integer and print it: