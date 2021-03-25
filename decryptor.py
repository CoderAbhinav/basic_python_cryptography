from cryptography.fernet import Fernet
from datetime import datetime

name = str(input("Enter the key name : "))

with open(f'data/{name}/key_{name}.key', 'rb') as my_key:
    key = my_key.read()

fernet = Fernet(key)

with open(f'data/{name}/data_{name}.txt', 'rb') as file:
    content = file.read()

decrypted_cont = fernet.decrypt(content)

z = decrypted_cont.decode('utf-8')
z = z.split('\n')
print(z)

with open(f'data/{name}/log_{name}.csv', 'a') as file:
    file.write(f"\nAccessed on,{datetime.now()}")
