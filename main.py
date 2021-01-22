amount=500
def deposit():
    print("\n Deposit page - \n")
    global amount
    dep = int(input("Enter the amount you want to deposit "))
    amount += dep


def withdraw():
    print("\n Withdraw page - \n")

    global amount
    wit = int(input("Enter the amount you want to withdraw "))
    if (amount - wit) >= 500:
        amount -= wit

    else:
        print("You cannot withdraw this much money because minimum balance of 500 should be maintained")


def details():
    global amount
    print("\n Details page - \n")
    print("Your balance is \n", amount)
    print("Thank you for being a part of our bank \n")


def main_():
    print("\n Welcome to the main page - \n")
    page = int(input(" Enter 1 if you want to visit Deposit page \n Enter 2 if you want to visit Withdraw page \n Enter 3 if you want to visit Details page"))
    if page == 1:
        deposit()
    if page == 2:
        withdraw()
    if page == 3:
        details()
