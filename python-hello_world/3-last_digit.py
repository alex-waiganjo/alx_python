#!/usr/bin/python3
import random
number = int(random.randint(-10000, 10000))
print(number)
num = int(str(number)[-1:]) 
if num>5:
    print(f"{num} is greater than 5")
elif num==0:
    print(f"{num} and is 0")
elif num<6 and num!=0:
    print(f"{num} and is less than 6 and not 0")