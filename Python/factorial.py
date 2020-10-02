#This program gives factorial of any number.

def factorial(int a):
    if(a == 1):
        return a
    else:
        return a*factorial(a-1)
i = int(input("enter the number"))
factorial(i)