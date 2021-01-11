#Question 3
#Assume we have list like this
#[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
#Basically a list of zero’s and one’s.
#Write a python function to the number of maximum consecutive  one’s present in the array. 
#E.g output for the above array would be 4


#Answer
def occurrences_of_one(lista):
    number_of_occurrences_of_one = 0
    maximum_number_of_occurrences_of_one = 0
    for i in list1:
        if i==1:
            number_of_occurrences_of_one = number_of_occurrences_of_one+1
            if number_of_occurrences_of_one>maximum_number_of_occurrences_of_one:
                maximum_number_of_occurrences_of_one=number_of_occurrences_of_one
        elif i==0:
            number_of_occurrences_of_one=0
        
    return(maximum_number_of_occurrences_of_one)
list1 = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
xy = occurrences_of_one(list1)
print(xy)
