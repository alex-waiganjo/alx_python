# #!/usr/bin/python3
# import random

# number = random.randint(-10000, 10000)

# last_digit = abs(number) % 10
# if number < 0:
#     last_digit = -last_digit

# message = f"The string Last digit of {number} is {last_digit}"

# if last_digit > 5:
#     message += " and is greater than 5"
# elif last_digit == 0:
#     message += " and is 0"
# else:
#     message += " and is less than 6 and not 0"

# print(message)
#!/usr/bin/python3
import random
number = int(random.randint(-10000, 10000))
num = int(str(number)[-1:]) 
if num>5:
    print(f"Last digit of {number} is {num} and  is greater than 5 \n")
elif num==0:
    print(f"Last digit of {number} is {num} and is 0 \n")
elif num<6 and num!=0:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0 \n")