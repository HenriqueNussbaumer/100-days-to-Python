
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_len = nr_numbers + nr_symbols + nr_letters #lembrar de colocar o -1 no total
password_char = []

i=0
for i in range(nr_letters):
    password_char.append(letters[random.randrange(1,52)])
i=0
for i in range(nr_letters):
    password_char.append(numbers[random.randrange(1,10)])
i=0
for i in range(nr_letters):
    password_char.append(symbols[random.randrange(1,9)])

random.shuffle(password_char)

password = ''
for i in password_char:
    password = password + i

print(password)



