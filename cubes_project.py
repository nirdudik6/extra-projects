import random
from time import sleep


while True:
    print("Lets start the game!")
    sleep(1)
    number=int(input("pick number between 1-6:\n"))
    if number <= 6:
        print("you chose "+str(number))
        print("lets roll!")
        sleep(3)
        cube = random.randint(1, 6)
        if cube == number:
            print("We got the same number and its " +str(cube))
        else:
            print("aww... its not the same number...\nyou chose "+str(number) + " and you got " + str(cube))

    else:
        print("choose only number between 1-6!!")
        continue

    exit=int(input("do you want to exit?\n1.yes\n2.no\n"))
    if exit == 1:
        break
    elif exit == 2:
        continue
print("thank you for playing :) bye bye!")

