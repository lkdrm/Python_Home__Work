#1 task:
# Write a function that calculates the sum of elements from
# a list of integers. The list is passed as a parameter:
"""
def sum_of_list(l):
    print("The sum of numbs is:", sum(l))

sum_of_list([1,2,3,4,5,6,7,8,9])
sum_of_list([2,4,6,8,10])
sum_of_list([9,12,5,7,0])
"""

#2 task:
#Write a function to find the maximum in the list of integers.
#The list is passed as a parameter:
"""
def max_of_list(l):
    print("The max of lst is:",max(l))

max_of_list([1,2,3,4,5,6,7,8,9])
max_of_list([22,333,-123,-10])
max_of_list([-2,-3,-5,-7,0,2])
"""
#3 task:
# Write a function that determines the number of even, odd,
# positive, negative elements in the list of integers. The list is
# passed as a parameter:

"""
def numbers(l):
    odd = []
    even = []
    neg = []
    pos = []
    for i in l:
        if i % 2 == 0 and i>0:
            odd.append(i)
        elif i % 2 == 1 and i>0:
            even.append(i)
        if i < 0:
            neg.append(i)
        elif i > 0:
            pos.append(i)
    print("All odd numbs:", odd, 
          "All even numbs:", even,
          "All negative numbs:",neg,
          "All positive numbs:", pos, sep="\n")

numbers([1,2,3,4,5,6,7,8,9,10,-2,-5,-6,-7,-3])
"""
#4 task:
# Write a function that flips the contents of the list of integers:            
"""
def flip(l):
    print(sorted(l,reverse=True))

flip([1,2,3,4,5,6,7,8,9])
flip(["hello","have","are","you"])
flip([4,6,2,20,11,-1])
"""
#5 task:
# Write a function that searches for some number in the
# list of integers.
"""
def find_numb(a):
    l = []
    for i in range(1,999):
        l.append(i)
    print("The index of the number:",l.index(a))

find_numb(50)
find_numb(25)
find_numb(1)
find_numb(99)
"""
#6 task:
# Write a function that calculates the factorial of each element
# in the list of integers. The function returns a new list
# containing the resulting factorials.

def the_numbers_of_factorial(l):
    factorials=[]
    d = 1
    for i in l:
        for f in range(1,i+1):
            


the_numbers_of_factorial([1,2,3])


