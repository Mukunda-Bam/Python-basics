import random
import pyautogui


chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
chars_list = list(chars)

password =pyautogui.password('enter a password: ')

guess_password =""

while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))
    print('<===================='+str(guess_password)+"<====================")

    if(guess_password == list(password)):
        print("you password is: "+ "".join(guess_password))
        break
