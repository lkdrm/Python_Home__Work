# task create a linear search:
my_list = [1, 3, 5, 7, 2, 8, 0,] # my list

my_number = 5 # I want to find a number 5

length_of_list = len(my_list) # find a length of my list

for index in range(0,length_of_list): # run in my list as index
    index_numb = 0 # here i save my result
    if my_list[index] == my_number: # if number of list is same , script will change a value of index_numb
        index_numb = index # save index
        print(index_numb)