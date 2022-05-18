import pyperclip, json
from pathlib import Path
import random

def printMenu():
    print("\n1 - Log in")
    print("2 - Register")
    print("3 - Exit\n")
    menuSelection = input("Enter Your Selection: ")
    while True:
        if menuSelection == '1':
            login()
            break
        elif menuSelection == '2':
            register()
            break
        elif menuSelection == '3':
            exit()
        else:
            print("\n1 - Log in")
            print("2 - Register")
            print("3 - Exit\n")

    print("\n1 - Find Password")
    print("2 - Add or update Password")
    print("3 - Delete Password")
    print("4 - Generate Password")
    print("5 - Exit\n")
    menuSelection = input("Enter Your Selection: ")
    while True:
        if menuSelection == '1':
            findPassword()
        elif menuSelection == '2':
            addPassword()
        elif menuSelection == '3':
            deletePassword()
        elif menuSelection == '4':
            generatePassword()
        elif menuSelection == '5':
            exit()
        else:
            print("Invalid Selection - Selections are case sensitive.")
        print("\n1 - Find Password")
        print("2 - Add or update Password")
        print("3 - Delete Password")
        print("4 - Generate Password")
        print("5 - Exit\n")
        menuSelection = input("Enter Your Selection: ")

    print("Finishing")
    print()


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    with open('passwords.json', mode='r') as file:
        data = json.load(file)
        file_username = data["Username"]
        file_username = decode(file_username)
        file_password = data["Password"]
        file_password = decode(file_password)
    
    if(username == file_username and password == file_password):
        print('Login successful')
    else:
        print('Login failed')
        exit()

def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    username = encode(username)
    password = encode(password)

    new_data = {
        "Username": username,
        "Password": password
    }                                                 
    try:
        with open('passwords.json', mode='w') as file:
            json.dump(new_data, file, indent=4)
    except FileNotFoundError:
        with open('passwords.json', mode='w') as file:
            json.dump(new_data, file, indent=4)

def findPassword():
    website = input("Enter Website: ")
    with open('passwords.json', mode='r') as file:
        data = json.load(file)
        password = data[website]["Password"]
        password = decode(password)
    print(f'Website : {website}\nPassword : {password}')
    pyperclip.copy(password)
    print("-Copied to clipboard-")

def addPassword():
    website = input("Enter Website: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    password = encode(password)
    new_data = {
        website: {
            "Email": email,
            "Password": password
        }
    }

    try:
        with open('passwords.json', mode='r') as file:
            data = json.load(file)
            data.update(new_data)
    except FileNotFoundError:
        with open('passwords.json', mode='w') as file:
            json.dump(new_data, file, indent=4)
    else:
        with open('passwords.json', mode='w') as file:
            json.dump(data, file, indent=4)

def deletePassword():
    website = input("Enter Website: ")
    with open('passwords.json', mode='r') as file:
        data = json.load(file)
        del data[website]
    with open('passwords.json', mode='w') as file:
        json.dump(data, file, indent=4)

def generatePassword():
    password = ''
    print("Generating new password.\n")
    length = int(input("Enter Desired Length of New Password: "))
    print()
    alphabet = chooseAlphabet()
    while(length > 0):
        length = length - 1
        password += random.choice(alphabet)
    print("Password = ", password)
    pyperclip.copy(password)
    print("-Copied to clipboard-")

def chooseAlphabet():
    alphabet = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print("Do you want your password to include: (y/n)")
    numbers = input("Numbers? ")
    specialCharacters = input("Special characters? ")
    if(numbers == 'y'):
        alphabet += '0123456789'
    if(specialCharacters == 'y'):
        alphabet += '!@#$%^&*()_-'
    return alphabet

def encode(password):
    encodedChars = []
    for i in range(len(password)):
        encodedChar = chr(ord(password[i]) - len(password))
        encodedChars.append(encodedChar)
    encodedPassword = "".join(encodedChars)
    return encodedPassword

def decode(encodedPassword):
    decodedChars = []
    for i in range(len(encodedPassword)):
        decodedChar = chr(ord(encodedPassword[i]) + len(encodedPassword))
        decodedChars.append(decodedChar)
    decodedPassword = "".join(decodedChars)
    return decodedPassword

printMenu()