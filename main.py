#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

for pwd_letters in range(0,nr_letters):
  pwd_letters = random.choice(letters)
  password += pwd_letters

for pwd_symbols in range(0,nr_symbols):
  pwd_symbols = random.choice(symbols)
  password += pwd_symbols

for pwd_numbers in range(0, nr_numbers):
  pwd_numbers = random.choice(numbers)
  password += pwd_numbers
print(password)
  


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

for pwd_letters in range(0,nr_letters):
  pwd_letters = random.choice(letters)
  password_list.append(pwd_letters)

for pwd_symbols in range(0,nr_symbols):
  pwd_symbols = random.choice(symbols)
  password_list.append(pwd_symbols)

for pwd_numbers in range(0, nr_numbers):
  pwd_numbers = random.choice(numbers)
  password_list.append(pwd_numbers)

random.shuffle(password_list)

password1 = ""
for pwd in password_list:
  password1 += pwd
print(password1)