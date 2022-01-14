"Practice modul 3 part 3 vše"
# Task 1:
# Calculate the following in a list filled with random numbers:
# ■ Sum of negative numbers;
# ■ Sum of even numbers;
# ■ Sum of odd numbers;
# ■ Product of elements with indices divisible by 3;
# ■ Product of elements between the smallest and the largest 
# element;
# ■ The sum of the elements between the first and the last 
# positive elements.

# Task 2:
# There is a list of integers filled with random numbers. Do 
# the following based on this data:
# ■ Create a list of integers containing only even numbers;
# ■ Create a list of integers containing only odd numbers;
# ■ Create a list of integers containing only negative numbers;
# ■ Create a list of integers containing only positive numbers
"""
import random

random_number = random.randrange(1,30)

def sum_of_numbers(my_number):
"""
print("This programm will create of one number:",
      "A list, will find and count all odd numbers and all even numbers",
      "Numbers divided by 3",sep="\n")
print("You just need to write a value.")
user = int(input("Enter a number:"))

def range_of_number(number): # The function will created with one number a list
    my_list = []
    if number < 0:
        for i in range(0,number-1,-1):
            my_list.append(i)
        return my_list
    for i in range(1,number+1):
        my_list.append(i)
    return my_list

def sum_of_list(my_list): # The function count a sum of list 
    if type(my_list) == list:
        return sum(my_list)
    return sum(range_of_number(my_list))

#def sum_of_negative_numbers(my_list): # The function count a sum of negative numbers
#    if type(my_list) == list:
#        return sum(my_list)
#    return sum(range_of_number(my_list)) 

def sum_of_even_numbers(my_list): # The function count a sum of even numbers
    even_list = [] #parni
    for i in range_of_number(my_list):
        if i%2 == 0:
            even_list.append(i)
    return sum_of_list(even_list)

def sum_of_odd_numbers(my_list): # The function count a sum of odd numbers
    odd_list = []
    for i in range_of_number(my_list):
        if i%2 == 1:
            odd_list.append(i)
    return sum_of_list(odd_list)

def numbers_divide_3(my_list): # The function find & count numbers divide 3
    list_divide = []
    for i in range_of_number(my_list):
        if i %3 == 0:
            list_divide.append(i)
    return sum_of_list(list_divide)

def find_and_count(my_list): # The function find & count max and min 
    sum_of_find = []
    sum_of_find.append(max(range_of_number(my_list)))
    sum_of_find.append(min(range_of_number(my_list)))
    return sum_of_list(sum_of_find)


def print_all(value):
    print("The range",range_of_number(value),
          "The sum of list:",sum_of_list(value),
          "The sum of even numbers:",sum_of_even_numbers(value),
          "The sum of odd numbers:",sum_of_odd_numbers(value),
          "The sum of divide by 3:",numbers_divide_3(value),
          "The sum of max and min of all range:",find_and_count(value),sep="\n")

print_all(user)


