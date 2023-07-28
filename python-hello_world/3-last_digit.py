#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", number, "is", number % 10, "and is", "greater than 5" if number % 10 > 5 else " 0" if number % 10 == 0 else "and is less than 6 and not 0")

# #!/usr/bin/python3
# import random
# number = int(random.randint(-10000, 10000))
# num = int(str(number)[-1:]) 
# if num>5:
#     print(f"Last digit of {number} is {num} and  is greater than 5 \n")
# elif num==0:
#     print(f"Last digit of {number} is {num} and is 0 \n")
# elif num<6 and num!=0:
#     print(f"Last digit of {number} is {num} and is less than 6 and not 0 \n")