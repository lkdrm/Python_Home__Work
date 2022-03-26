import matplotlib.pyplot as plt
from about__numpy import MyNumpy as my_lst

my_list = my_lst
my_list_of_numbers = my_list.arange(20)
my_list_of_numbers_2 = my_list_of_numbers + 1
my_list_of_numbers_3 = my_list_of_numbers + 2
my_list_of_numbers_4 = my_list_of_numbers + 3
my_list_of_numbers_5 = my_list_of_numbers + 4
my_list_of_numbers_6 = my_list_of_numbers + 5
numbers = range(1,len(my_list_of_numbers)+1)

print(numbers)
fig,ax = plt.subplots(figsize = (11,6))
ax.scatter(numbers,my_list_of_numbers,   s = 150, c = list(range(len(my_list_of_numbers))), cmap="viridis", label = "normal",)
ax.plot(numbers,my_list_of_numbers_2,    lw = 2,  ls = "dotted",  c = "green", label = "count+1",)
ax.scatter(numbers,my_list_of_numbers_3, s = 200, c = list(range(len(my_list_of_numbers_3))), label = "count+2",)
ax.plot(numbers,my_list_of_numbers_4,    lw = 4,  ls = "dashdot", c = "pink", label = "count+3",)
ax.scatter(numbers,my_list_of_numbers_5, s = 250, c = list(range(len(my_list_of_numbers_5))), cmap ="inferno",label = "count+4",)
ax.plot(numbers,my_list_of_numbers_6,    lw = 6,  ls = "solid",   c = "black", label = "count+5",)
ax.legend()

plt.show()

