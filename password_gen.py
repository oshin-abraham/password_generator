# password = shuffled, random, letters, numbers.... secret code
# qwdg457!@

import random
letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers= ['1','2','3','4','5','6','7','8','9']
symbols= ['@','#','^','*','()','&']

print("Welcome to Password Generator")
n_letters= int(input("How many letters you need in password?\n"))
n_numbers= int(input("How many numbers do you need for your password?\n"))
n_symbols= int(input("How many symbols do you need for your password?\n"))

password= " "

for x in range(1, n_letters+1):
    char= random.choice(letters)
    password= password + char


for x in range(1, n_numbers+1):
    char= random.choice(numbers)
    password= password+char


for x in range(1,n_symbols+1):
    char= random.choice(symbols)
    password= password+char
print(password)