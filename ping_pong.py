print("Welcome to my ping pong project")
name1=input("Put the first name:\n")
name2=input("Put the second name:\n")
print("the result is:\n" + name1 + ":0\n" + name2 + ":0\n")
point1 = 0
point2 = 0
while (point2 < 11) and (point1 < 11):
    point_num=input("who won the point?\n1." + name1 + "\n2. " + name2 + "\n")
    if (point_num == "1"):
        point1= point1 + 1
    elif (point_num == "2"):
        point2 = point2 + 1
    else:
        print("wrong number!!")
    print("the result is:\n" + name1 + ":" + str(point1) + "\n" + name2 + ":" + str(point2) + "\n")
print("game over!")
