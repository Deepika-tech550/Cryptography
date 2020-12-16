#Cryptography is nothing but the normal message->convert to a secrete message and the secrete code is saved by sender
#and the secrete message is decoded by reciever with the help of secrete

#import cryptography.fernet()

from cryptography.fernet import Fernet

#1 generate key and write that in a password.txt"
def generate_key():
    global key
    key=Fernet.generate_key()
    return "key",key
    abc=open("password.txt",'wb')  #open file

    return "the password saved in password.txt file "
    abc.write(key)
    abc.close()

#2 read th password in password.txt file or getting key
def read_generate_password():
    ab=open("password.txt",'r')
    return "reading the password",ab.read()
    ab.close()

#3 getting content from user to encrypt

def user_message():
    global msg
    msag=input("enter message to encryprt")
    msg=msag.encode()
   


#4 Encrypt
def encrypt(message):
    
    f=Fernet(key)
    global token
    token = f.encrypt(message)
    return "encrypted message",token
   

#5 decrypt()
def decrypt():
    f=Fernet(key)
    demsg=f.decrypt(token)
    
    return "decrypted message",demsg




g=generate_key()
r=read_generate_password()
u=user_message()
e=encrypt(msg)   
d=decrypt()



print(e)
print(d)
