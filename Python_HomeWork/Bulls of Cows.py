"""
Develop a game of Bulls and Cows. The program chooses
a four-digit number, and the player has to guess it. After
the user enters a number, the program reports how many digits of
the number are guessed (bulls), and how many digits are guessed
and stand in the right place (cows). After guessing the number,
print the number of user’s attempts. Use recursion in your game.

"""
import random


number = str(random.randint(1000,9999)) # creat a number

def list_of_number(number): # create of one long number list 
    list_of_numbers = []
    for i in number: # do the cicle of number 
        list_of_numbers.append(i)
    return list_of_numbers

print(list_of_number(number))

def user_number(user):
    list_of_user_number = []
    #user = input("Enter your number:")
    for i in user:
        list_of_user_number.append(i)
    return list_of_user_number

print(user_number("2475"))