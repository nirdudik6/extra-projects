ticket=input("Did you get a new ticket?(yes/no) ")
if (ticket=="yes"):
    site=input("Enter which site is the ticket about:(israel/ukraine/malta) ")
    if site=="israel":
        subject = input("enter the number of subject:\n1.device request\n2.backend\n3.brands\n4.connection issue\n5.hardware issue\n6.it internal\n7.office 365\n8.phone system\n9.security/permissions\n10.software\n11.user's account\n12.HR request\n ")
        if subject=="1":
            print("it should assigne it to nir!")
        elif subject=="2":
            print("it should assigne it to nir!")
        elif subject=="12":
            print("it should assigne it to nir!")
        elif subject=="3":
            print("it should assigne it to liran!")
        elif subject=="4":
            print("it should assigne it to nir!")
        elif subject=="5":
            print("it should assigne it to nir!")
        elif subject=="6":
            print("it should assigne it to nir!")
        elif subject=="7":
            print("it should assigne it to nir!")
        elif subject=="8":
            print("it should assigne it to matej!")
        elif subject=="9":
            print("it should assigne it to liran!")
        elif subject=="10":
            print("it should assigne it to nir!")
        elif subject=="11":
            print("it should assigne it to nir!")
    elif site=="ukraine":
        subject = input("enter the number of subject:\n1.device request\n2.backend\n3.brands\n4.connection issue\n5.hardware issue\n6.it internal\n7.office 365\n8.phone system\n9.security/permissions\n10.software\n11.user's account\n12.HR request\n ")
        if subject=="1":
            print("it should assigne it to oleh!")
        elif subject=="2":
            print("it should assigne it to nir!")
        elif subject=="12":
            status=input("Is the changing rules or on/offboarding?(1.on/offboarding\n2.changing rule\n")
            if status == "1":
                print("it should assigne it to oleh!")
            elif status == "2":
                print("it should assigne it to matej!")
        elif subject=="3":
            print("it should assigne it to alex and if he can't do it so assigne it to liran!")
        elif subject=="4":
            print("it should assigne it to oleh and if he can't do it so assigne it to nir!")
        elif subject=="5":
            print("it should assigne it to oleh and if he can't do it so assigne it to nir!")
        elif subject=="6":
            print("it should assigne it to nir!")
        elif subject=="7":
            print("it should assigne it to oleh and if he can't do it so assigne it to nir!")
        elif subject=="8":
            print("it should assigne it to matej!")
        elif subject=="9":
            print("it should assigne it to liran!")
        elif subject=="10":
            print("it should assigne it to oleh and if he can't do it so assigne it to matej!")
        elif subject=="11":
            print("it should assigne it to oleh and if he can't do it so assigne it to matej!")
    elif site=="malta":
        subject = input("enter the number of subject:\n1.device request\n2.backend\n3.brands\n4.connection issue\n5.hardware issue\n6.it internal\n7.office 365\n8.phone system\n9.security/permissions\n10.software\n11.user's account\n12.HR request\n ")
        if subject=="1":
            print("it should assigne it to matej!")
        elif subject=="2":
            print("it should assigne it to nir!")
        elif subject=="12":
            print("it should assigne it to matej!")
        elif subject=="3":
            print("it should assigne it to liran!")
        elif subject=="4":
            print("it should assigne it to nir!")
        elif subject=="5":
            print("it should assigne it to matej!")
        elif subject=="6":
            print("it should assigne it to nir!")
        elif subject=="7":
            print("it should assigne it to matej!")
        elif subject=="8":
            print("it should assigne it to matej!")
        elif subject=="9":
            print("it should assigne it to liran!")
        elif subject=="10":
            print("it should assigne it to matej!")
        elif subject=="11":
            print("it should assigne it to matej!")
elif (ticket=="no"):
    print("so there is no problem :)")

