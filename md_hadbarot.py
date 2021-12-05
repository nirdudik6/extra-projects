import pywhatkit as pywhatkit

print("Hey! welcome to MD Hadbarot!")
while (True):
    mazik=input("Which kind of pests do you have? (Cockroaches/Ants/other)\n")
    if mazik == "Cockroaches" or mazik == "cockroaches":
        kind=input("which kind of Cockroaches do you have?\n if german enter 1\n if other kind enter 2\n")
        if kind=="1":
            kind="german"
            gel=input("Do you want to add gel with it? yes/no (it's an additional cost)\n")
            if gel=="yes":
                print ("added!")
            elif gel=="no":
                print("ok let continue")
        elif kind=="2":
            kind = "other"
            gel="no of course"
        home = input("which kind of house do you have? private/apartment\n")
        note = input("write some information about your home like how many rooms do you have or if you have balcony:\n")
        msg = "I have " + mazik + ", the type is " + kind + ", gel: " + gel + ", home type: " + home + ", other information: " + note
        hour = int(input("enter the hour of sending:\n"))
        min = int(input("enter the minutes of sending:\n"))
        pywhatkit.sendwhatmsg(his phone, msg, hour, min)
        print("sent!")
        break
    elif mazik == "Ants" or mazik == "ants":
        kind = input("which kind of ants do you have?\n")
        house = input("which kind of house do you have? private/apartment\n")
        addition = input("write some information about your home like how many rooms do you have or if you have balcony:\n")
        msg= "I have " + mazik + ", the type is " + kind + ", home type: " + house + ", other information: " + addition
        hour = int(input("enter the hour of sending:\n"))
        min = int(input("enter the minutes of sending:\n"))
        pywhatkit.sendwhatmsg(his phone, msg, hour, min)
        print("sent!")
        break
    elif mazik == "Other" or mazik == "other":
        kind = input("which kind of mazik do you have?\n")
        house = input("which kind of house do you have? private/apartment\n")
        addition = input("write some information about your home like how many rooms do you have or if you have balcony:\n")
        msg = "I have " + mazik + ", the type is " + kind + ", home type: " + house + ", other information: " + addition
        hour = int(input("enter the hour of sending:\n"))
        min = int(input("enter the minutes of sending:\n"))
        pywhatkit.sendwhatmsg(his phone, msg, hour, min)
        print("sent!")
        break
    else:
        print("choose only these options :/\n")
        continue
