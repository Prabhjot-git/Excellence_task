#Write a function in python in python, which will return maximum i.e function
#should return dictionary like
#{
#  “3” : 70
#}

#Answer:
def max_of_marks(dicta):
    maxx = 0
    for i in dicta:
        if maxx < dicta[i]:
            maxx = dicta[i]
    return(maxx)
dict1 = {
    '1' : 50,
    '2' : 60,
    '3' : 40,
    '4' : 20,
    '5' : 80,
    '6' : 90,
    '7' : 30,
    '8' : 70,
    '9' : 20,
    '10' : 10,
    '11' : 90,
    '12' : 97,
    '13' : 30,
    '14' : 54,
    '15' : 56,
    '16' : 53,
    '17' : 51,
}
xy = max_of_marks(dict1)
print(xy)
