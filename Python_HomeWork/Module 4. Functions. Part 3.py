# Task 1:
# Write a recursive function to find the power of a number:

a = 2

def power_of_number(number):
    result = number**2
    return result

print(power_of_number(a))

# Task 2:
# Write a recursive function that calculates the sum of all
# numbers in the range from a to b. The user types in a and b.
# Illustrate how the function works with an example:

a = 1
b = 5

def created_range(a,b): # created a range
    result = []
    while a <= b: 
        result.append(a)
        a+=1
    return result
print(created_range(a,b))

def sum_of_numb(list_of_numb): # count a sum
    count = 0
    i = 0
    while i <len(list_of_numb):
        count += list_of_numb[0+i]  
        i+=1
    return count

print(sum_of_numb(created_range(a,b)))

# Task 4:
# Develop a game of Tic-tac-toe.

