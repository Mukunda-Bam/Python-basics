import random

password = input("please input your password: ")

guess_password= ""

char = 'abcdefghijklmnopqrstuvwxyz'

char_list = list(char)

while guess_password != password:
    guess_password =random.choices(char_list, k=len(password))
    print(f'******* {guess_password} *******')

    if guess_password ==list(password):
        print(f'password is : {guess_password}')
        break