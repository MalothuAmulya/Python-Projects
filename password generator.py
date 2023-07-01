import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*','(', ')', '+']
print("Welcome to password generator")
n_letter=int(input("How many letters do you want in your password?\n"))
n_symbols=int(input("How many symbols do you want in your password?\n"))
n_numbers=int(input("How many numbers do you want in your password?\n"))
password_list=[]
for i in range(1,n_letter+1):
    char = random.choice(letters)
    password_list += char
for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    password_list += char
for i in range(1,n_numbers+1):
    char = random.choice(numbers)
    password_list += char
#print(password_list) - before shuffling
random.shuffle(password_list)
# print(password_list) - after shuffling
password=""
for char in password_list:
    password += char
print("Your customised password is :")
print(password)