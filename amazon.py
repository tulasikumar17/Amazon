adl={"admin1":{"password":"a111"},"admin2":{"password":"a222"}}
merl={"mer1":{"password":"m111"}}
ul={"user1":{"password":"u111","wallet":200,"orders":{}},
       "user2":{"password":"u222","wallet":500,"orders":{}}}
apme={}
aprej={}
def newuser():
    pass
def existuser():
    print("Enter your username:")
    us=input()
    print("Enter your password:")
    uspas=input()
    if ul[us]["password"]==uspas:
        print(us,"Succesfully logged in")
    else:
        print("Invalid password")
        input("\tpress enterto continue")
def newmerchant():
    print("Enter your username:")
    meus=input()
    print("Enter a password:")
    meepas=input()
    if meus not in merl:
        if meus not in apme:
            a={meus:{"password":meepas}}
            apme.update(a)
            print("requested")
            input("\tPress enter to continue")
    else:
        print("invalid username change it:")
        input("\tEnter to continue")
def existmerchant():
    print("Enter your username:")
    me=input()
    print("Enter your password:")
    mepas=input()
    if me not in aprej:
        if me not in apme:
            if me in merl:
                if merl[me]["password"]==mepas:
                    print(me,"Succesfully logged in")
                    while True:
                        print("1.Add products\n2.Remove products\n3.orders\n4.Exit")
                        mech=int(input("Enter your Choice :"))
                        if mech==1:
                            pass
                        elif mech==2:
                            pass
                        elif mech==3:
                            pass
                        elif mech==4:
                            break
                        else:
                            print("Invalid Input")
                else:
                    print("Invalid login credentials")
                    input("\tpress Enter to continue")
            else:
                print("you are not existing merchant")
                input("\tpress Enter to continue")
        else:
            print("your request is in progress")
            input("\tpress Enter to continue")
    else:
        print("your request is rejected")
        print("Please! contact admistrator")
        input("\tpress Enter to continue")
def addmerchants():
    if len(apme)!=0:
        print("new approve requests")
    else:
        print("no new requests")
def approvemerch():
    if len(apme)!=0:
        print(*apme.keys())
        print("enter merchant to approve or reject")
        asm=input()
        print("Enter 1 to approve\nEnter 0 to reject",asm)
        apmr=input()
        apme_w={asm:apme[asm]}
        if apmr=="1":
            apme_copy={**apme}
            for i in apme_copy.keys():
                if i==asm:
                    merl.update(apme_w)
                    apme.pop(i)
            print("suucesfully approved")
            input("\tpress Enter to continue")
        elif apmr=="0":
            apme_copy={**apme}
            for i in apme_copy.keys():
                if i==asm:
                    aprej.update(apme_w)
                    apme.pop(i)
            print("Request Rejected")
            input("\tpress Enter to continue")
    else:
        print("No approvals")
        input("\tpress Enter to continue")
def removemer():
    print("enter merchant to remove",end=":")
    print(*merl.keys())
    mrem=input()
    if mrem in merl:
        merl.pop(mrem)
        print("succesfully removed",mrem)
        input("Press enter to show merchant list")
        print(*merl.keys())
        input("\tPress enter to continue")
    else:
        print("Invalid merchant")
def admin():
    print("Enter your username:")
    ad=input()
    print("Enter your password:")
    adpas=input()
    if adl[ad]["password"]==adpas:
        print(ad,"Succesfully logged in")
        while True:
            print("1.Approve merchants\n2.Remove merchants\n3.Approve users\n4.Exit")
            adch=int(input("Enter your Choice :"))
            if adch==1:
                approvemerch()
            elif adch==2:
                removemer()
            elif adch==3:
                pass
            elif adch==4:
                break
            else:
                print("Invalid Input")
    else:
        print("Invalid Login credentials")
        input("\tPress Enter to continue")
def merchant():
    while True:
        print("1.New merchant\n2.Existing merchant\n3.Exit")
        me=input("Enter your choice:")
        if me=="1":
            newmerchant()
        elif me=="2":
            existmerchant()
        elif me=="3":
            break
        else:
            print("invalid input")
def user():
    while True:
        print("1.New user\n2.Existing user\n3.Exit")
        print("Enter your choice:")
        us_i=input()
        if us_i=="1":
            newuser()
        elif us_i=="2":
            existuser()
        elif us_i=="3":
            break
        else:
            print("Invalid input")
            input("\tpress enterto continue")
def orders():
    print("inside orders")
while True:
    print("\tWelacome to Amazon")
    print("1.Admin\n2.Merchant\n3.User\n4.exit")
    print("Enter your choice")
    a=input()
    if a=="1":
        admin()
    elif a=="2":
        merchant()
    elif a=="3":
        user()
    elif a=="4":
        break
    else:
        print("Invalid Input")