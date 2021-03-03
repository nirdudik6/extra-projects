


print("hello there, welcome to my bank project!\n")
while (True):
    print("there is your available accounts:\ncash\nbank account\n")
    bank_account=int(input("enter your bank account:\n"))
    cash = int(input("enter your cash:\n"))
    print("your bank account has " + str(bank_account) + " and your cash has " + str(cash))
    activity=input("enter your choice:\n1.change your cash\n2.change your bank account\n")
    if activity=="1":
        move=input("what do you want to do?\n1.add money\n2.drain my money\n3.move the money to the bank account\n")
        if move=="1":
            money = int((input("how many cash do you want to add?\n")))
            print("your total cash is " + str(cash + money))
        elif move=="2":
            menos = int((input("how many cash do you want to remove?\n")))
            print("your total cash is " + str(cash - menos))
        elif move=="3":
            deliver = int((input("how many cash do you want to deliver to the bank account?\n")))
            print("your total cash is " + str(cash - deliver))
            print("your total bank account is " + str(bank_account + deliver))
        else:
            print("choose 1-3 only!!")
    elif activity=="2":
        bank=input("what do you want to do?\n1.add money\n2.drain my money\n3.move the money to the cash\n")
        if bank=="1":
            money_2 = int((input("how many money do you want to add?\n")))
            print("your total cash is " + str(bank_account + money_2))
        elif bank=="2":
            menos_2 = int((input("how many money do you want to remove?\n")))
            print("your total cash is " + str(bank_account - menos_2))
        elif bank=="3":
            deliver_2 = int((input("how many money do you want to deliver to the cash?\n")))
            print("your total bank account is " + str(bank_account - deliver_2))
            print("your total cash is " + str(cash + deliver_2))
        else:
            print("choose 1-3 only!!")
    else:
        print("choose only 1-2!!!")
        continue
    if (input("do you want to exit? y/n\n") == "y"):
        break
    print("thanks and bye bye...")
