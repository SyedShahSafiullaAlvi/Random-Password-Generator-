import random               # importing required modules
import time

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Python Random Password Generator.")

number_of_numbers=int(input("How many numbers you want in pssword? "))
number_of_letters=int(input("How many case letters you want in pssword? "))
number_of_symbols=int(input("How many symbols you want in pssword? "))

password=''             # initializing a empty string


for char in range(1,number_of_letters+1):           # concatenating n numbers of numbers to empty string
    password+=random.choice(letters)

for char in range(1,number_of_symbols+1):           # concatenating n numbers of letters to password string
    password+=random.choice(symbols)

for char in range(1,number_of_numbers+1):           # concatenating n numbers of symbols to password string
    password+=random.choice(numbers)
#  got a string as password, but it is like n numbers + n letters + n symbols 
#  to make password more powerfull, I am shuffling the password string
final_password=''.join(random.sample(password,len(password)))

print("Wait for few seconds. Password is generating...")
time.sleep(3)
print(final_password)               # finally got a shuffled password
        


