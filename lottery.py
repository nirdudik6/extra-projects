import random
from time import sleep


print("hello to my lottery! :)")
bet=int(input("Enter the number of Lotteries that you want to do:\n"))

for i in range(0,bet):
    print("\nso lets start!\n")
    sleep(5)
    lottery_numbers = []
    for x in range(6):
        number = random.randint(1,37)
        while number in lottery_numbers:
            number = random.randint(1, 37)
        lottery_numbers.append(number)
    print("the numbers are " + str(lottery_numbers))
    print("\nAnd the spacial number is...\n")
    spec_number = random.randint(1,7)
    print(spec_number)
    print("\n------------------------------\n")
    print("\nso finally the numbers are:\n")
    print("\n" + str(lottery_numbers) + " " + str(spec_number) + "\n")



