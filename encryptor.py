from cryptography.fernet import Fernet
from datetime import datetime
import os

with open('data/key_names.txt' ,'r') as used_key:
    all_keys = used_key.read()

print("Program to encrypt your email & password")
z = str(input("Create a key name : "))
while z in all_keys:
    print("Sorry that key name is already taken.")
    z = str(input("Write a new key name : "))

x = str(input("Please enter email : "))
y = str(input("Please enter password : "))

os.mkdir(f'data/{z}')

with open(f"data/{z}/data_{z}.txt", "w") as store:
    store.write(x)
with open(f'data/{z}/data_{z}.txt','a') as store:    
    store.write(f'\n{y}')



key = Fernet.generate_key()

with open(f'data/{z}/key_{z}.key' , 'wb') as my_key:
    my_key.write(key)

with open(f'data/{z}/key_{z}.key', 'rb') as file:
    e_key = file.read()

fernet = Fernet(e_key)

with open(f'data/{z}/data_{z}.txt', 'rb') as file:
    content = file.read()

encrypted_cont = fernet.encrypt(content)

with open(f'data/{z}/data_{z}.txt', 'wb') as file:
    file.write(encrypted_cont)


with open(f'data/{z}/log_{z}.csv', 'a') as file:
    file.write("Event,time")
    file.write(f"\nCreated on,{datetime.now()}")

with open(f"data/key_name.txt", 'a') as file:
    file.write(f"{z}")
