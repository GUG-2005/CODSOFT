from random import *

#Characters for random strong passwords
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Password characters
password_let = [choice(letters) for i in range(randint(8, 10))]
password_sym = [choice(numbers) for j in range(randint(4, 5))]
password_num = [choice(symbols) for k in range(randint(4, 5))]

#Password list
password_list = password_let + password_sym + password_num
shuffle(password_list)
password = ''.join(password_list)

#get input length from the user
pas = password
inp = int(input("What is the length of your password: "))

if inp <8 or inp>15:
    print("The length should be between 8 to 15 characters.")
else:
    p = ""
    for i in range(inp):
        p += pas[i]
    print(f"Your Susggested password is: {p}")