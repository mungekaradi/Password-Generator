import random 
import string

print("Aditya's random password generator")

def myPass():
    length = int(input("enter length of password"))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = string.digits
    special = string.punctuation

    combine = lower + upper + number + special

    x = random.sample(combine, length)      # sample will return new value.
    password ="".join(x)        # convert list into string.
    print(password)
    myPass()            # call the function repeatedly.
myPass()
