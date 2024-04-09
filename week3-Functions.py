#Functions, need a input and a output 

def function(a):
    """add 1 to a"""
    b=a+1;
    print(a, "+1 =", b)
    return b
#Functions are used to make the code cleanner and faster!

# function(5)
#the function above is make a plus 1 sum and printing the result

# c = function(20)
#we can add functions in variables

album_ratings=[10.0,8.5,9.5]

def printStuff(x):
    for i,s in enumerate(x):
        print("Album", i, "rating is ", s)

printStuff(album_ratings)


print(len([sum([1,1,1])]))

L=[1,3,2]

print(sorted(L))