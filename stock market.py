from selenium import webdriver
from time import sleep

while True:
    print("welcome to the menu\n")
    options=input("what do you want to do?\n1.see stock's information\n2.change stock's list\n")
    if options=="1":
        stock=input("enter the stock's symobol you are looking for:\n")
        driver = webdriver.Chrome(#chromedriver route)
        driver.get("https://finviz.com/quote.ashx?t="+ stock)
        sleep(2)
        exit=input("Do you want to exit?(yes/no)\n")
        if exit=="yes":
            print("bye bye :)")
            break
        elif exit=="no":
            continue
    elif options=="2":
        print("here is your stock's list:\n")
        sleep(2)
        stock_list = #t.x.t route
        file1 = open(stock_list, "r")
        print(file1.read())
        action=input("What do you want to do?\n1.add\n2.remove\n")
        if action=="1":
            stock=input("Enter the symbol that you want to add:\n")
            stock_list = open(stock_list, "r")
            stock_list = stock_list.read().splitlines()
            if stock in stock_list:
                print("sorry this stock is already on list :( ")
                sleep(2)
                exit = input("Do you want to exit?(yes/no)\n")
                if exit == "yes":
                    print("bye bye :)")
                    break
                elif exit == "no":
                    continue
            else:
                print("this stock isn't in the list!\n")
                add = input("Do you want to add this stock?\n")
                if add == "yes":
                    stock_list = #t.x.t route
                    fin = open(stock_list, "a")
                    fin.write("\n" + stock)
                    fin.close()
                    print("stock added to the list!\n")
                    sleep(3)
                    exit = input("Do you want to exit?(yes/no)\n")
                    if exit == "yes":
                        print("bye bye :)")
                        break
                    elif exit == "no":
                        continue
                elif add=="no":
                    print("so lets move you to the main menu\n")
                    sleep(2)
                    continue
        elif action=="2":
            remove= input("Enter the symbol that you want to remove:\n")
            stock_list = #t.x.t route
            stock_list = open(stock_list, "r")
            stock_list = stock_list.read().splitlines()
            if remove in stock_list:
                with open(#t.x.t route, "r") as f:
                    lines = f.readlines()
                with open(#t.x.t route, "w") as f:
                    for line in lines:
                        if line.strip("\n") != remove:
                            f.write(line)
                print("stock removed from the list!\n")
                sleep(3)
                exit = input("Do you want to exit?(yes/no)\n")
                if exit == "yes":
                    print("bye bye :)")
                    break
                elif exit == "no":
                    continue
            else:
                print("this stock isn't in the list!\n")
                sleep(3)
                exit = input("Do you want to exit?(yes/no)\n")
                if exit == "yes":
                    print("bye bye :)")
                    break
                elif exit == "no":
                    continue
    else:
        print("choose only 1 or 2!!!")
        sleep(2)
        continue

