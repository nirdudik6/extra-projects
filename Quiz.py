from time import sleep


def quiz():
    print("so lets start with the first question:\n")
    sleep(2)
    year=input("Which year was Nir born?\n1.2000\n2.2001\n3.1998\n4.1995\n")
    if year=="3":
        sleep(2)
        print("correct!\n")
    elif year=="1" or year=="2" or year=="4":
        sleep(2)
        print("incorrect!\n")
    print("so lets start with the second question:\n")
    sleep(2)
    month = input("Which month was Nir born?\n1.october\n2.january\n3.may\n4.november\n")
    if month=="1":
        sleep(2)
        print("correct!\n")
    elif month=="3" or month=="2" or month=="4":
        sleep(2)
        print("incorrect!\n")
    print("so lets start with the third question:\n")
    sleep(2)
    hobby = input("What was nir's hobby when he was a teenager?\n1.football\n2.basketball\n3.badminton\n4.hokey\n")
    if hobby == "3":
        sleep(2)
        print("correct!\n")
    elif hobby == "1" or hobby == "2" or hobby == "4":
        sleep(2)
        print("incorrect!\n")
    print("so lets start with the fourth question:\n")
    sleep(2)
    age = input("How old is Bobi?\n1.16\n2.15\n3.20\n4.10\n")
    if age == "1":
        sleep(2)
        print("correct!\n")
    elif age == "3" or age == "2" or age == "4":
        sleep(2)
        print("incorrect!\n")
    print("so lets start with the fifth question:\n")
    sleep(2)
    work = input("where does nir work?\n1.intel\n2.aspireglobal\n3.jfrog\n4.continet\n")
    if work == "2":
        sleep(2)
        print("correct!\n")
    elif work == "3" or work == "1" or work == "4":
        sleep(2)
        print("incorrect!\n")




while True:
    quiz()
    Exit = input("Do you want to quit?(yes/no)\n")
    Exit = Exit.upper()
    if Exit == "NO":
        continue
    elif Exit == "YES":
        break
print("bye! hope to see you soon!")