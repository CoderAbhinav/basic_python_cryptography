from cryptography.fernet import Fernet
import os

##this key will be constant
key =  b'jAvAN8ZXJKfLs6blqY8dk8BpxlrcdmOxzo4K8LZrWyI='
fernet = Fernet(key)

def encrypt_data(x,y):
    encrypted_email = fernet.encrypt(bytes(x, 'utf-8'))
    encrypted_pass = fernet.encrypt(bytes(y, 'utf-8'))
    
    with open("data.txt" ,'wb') as f:
        f.write(encrypted_email)
        f.write(b'\n')
        f.write(encrypted_pass)
    f.close()

def decrypt_data(token):
    
    d = fernet.decrypt(token)
    print(d.decode())


##this part will be in our main program
if not (os.path.isfile("data.txt")):
    x = str(input("Please enter email : "))
    y = str(input("Please enter password : "))
    encrypt_data(x,y)
else:
    with open("data.txt",'rb') as f:
        email = f.readlines(1)
        password = f.readlines(2)
    decrypt_data(email[0])    
    decrypt_data(password[0])    
    f.close()

