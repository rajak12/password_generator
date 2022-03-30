import random

print('welcome to your password generator')

chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?1234567890'

number = input('amount  of password to generate :')
number = int(number)

length = input('your password length:')
length = int(length)

print('\nhere are your password:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars) 
    print(passwords)
