#Question1
#Use python lists and make a list of numbers.
#Write a function which returns sum of the list of numbers

#Answer:
#There are two ways for getting the sum of elements of List

#1. Using Iterative Way:
def sum_of_list(lista):
    c = 0
    for i in lista:
        c = c+i
    return c
list1 = [10,23,4,58,9,67]
xy = sum_of_list(list1)
print(xy)

# 2. Using built-in Function of Python Sum()
def sum_number(lista):
    c = sum(lista)
    return c
list1 = [10,23,4,58,9,67]
xy = sum_number(list1)
print(xy)
