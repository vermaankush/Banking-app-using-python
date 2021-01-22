from random import randint
from main import *
from acno import *
from reg import *

e=1
l=1
em="@gmail.com"
em2=0
while e==1:
    print(" BANKING APPLICATION \n")
    user=int(input("press 0 if existing user , press 1 if new user   "))
    if user==1:
            reg()
    if l!=1:
        break
    if user==0:
        login()

    mains=1
    while mains==1:
        main_()
        mains = int(input("\nEnter 1 if want to go to main page \nEnter any other number to continue "))
    Exit=int(input("\nEnter 1 if you want to restart the banking application \nEnter any other number to exit "))
    if Exit!=1:
        break



