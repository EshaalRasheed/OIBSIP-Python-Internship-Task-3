import random
print("...............Welcome to Random Password Generator.............")
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoqrstuvwxyz"
numbers="0123456789"
symbols=['@','!','#','$','%','^','&','*','(',')']
length=int(input("Enter the length of password : "))
n_letters=int(input("How many letters you want to enter ?"))
n_symbols=int(input("How many symbols you want to enter ?"))
n_numbers=int(input("How many numbers you want to enter ?"))
password=" "
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password+=char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password+=char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password+=char
print(password)        



