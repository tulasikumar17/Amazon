import os
adl={"admin1":{"password":"a111"},"admin2":{"password":"a222"}}
merl={"mer1":{"password":"m111","products":{}}}
ul={"user1":{"password":"u111","wallet":25000,"cart":{},"previous orders":{}},
       "user2":{"password":"u222","wallet":50000,"cart":{},"previous orders":{}}}
prd={"categories":
    {"mobiles":{"Mi":{"name":"6 pro","cost":12000,"quantity":5},"oppo":{}},"laptops":{"hp":{},"dell":{}},"food products":{"chocolates":{},"chips":{}}}}
apme={}
aprej={}
def buypr(us_po,adc,ad_p):
    print("Enter the quantity you want to buy")
    bu_p=input()
    try:
        if int(bu_p)<prd["categories"][adc][ad_p]["quantity"]:
            ab_c=prd["categories"][adc][ad_p]["cost"]
            if int(bu_p)*ab_c<=ul[us_po]["wallet"]:
                print("Total cost is :",int(bu_p)*prd["categories"][adc][ad_p]["cost"])
                as_p={adc:{"name":prd["categories"][adc][ad_p]["name"],"cost":int(bu_p)*prd["categories"][adc][ad_p]["cost"],"quantity":int(bu_p)}}
                ul[us_po]["wallet"]=ul[us_po]["wallet"]-int(bu_p)*ab_c
                ul[us_po]["previous orders"].update(as_p)
                print("Your order is succefully placed")
                input("\tPress Enter to continue")
            else:
                print("You don't have sufficient balance in your wallet")
                input("\tPress Enter to continue")
        else:
            print("The selected quantity is unavalable")
            input("\tPress Enter to continue")
    except:
        print("Quantity must be a number")
        input("\tPress Enter to continue")
def cartadd(us_po,adc,ad_p):
    as_p={adc:{"name":prd["categories"][adc][ad_p]["name"],"cost":prd["categories"][adc][ad_p]["cost"]}}
    ul[us_po]["cart"].update(as_p)
    print("Your order is succefully added to cart")
    input("\tPress Enter to continue")
def prevord(us):
    print("\tPrevious orders")
    co_u=0
    for i in ul[us]["previous orders"].keys():
        co_u=co_u+1
        print("\tOrder -->",co_u)
        print(i)
        for j in ul[us]["previous orders"][i].keys():
            print(j,end="-->")
            print(ul[us]["previous orders"][i][j])
        input("\tPress Enter to continue")
def adprt():
    print("please select product category to add :")
    print(*prd["categories"].keys(),sep=" or ")
    adc=input("Enter category to add :")
    try:
        if adc in prd["categories"].keys():
            print(*prd["categories"][adc].keys(),sep=" or ")
            ad_p=input("Enter name of product :")
            print("cost of product:")
            try:
                ad_c=int(input())
                ad_q=input("Enter Quantity to add :")
                if ad_c>0:
                    ad_up={"categories":{adc:{ad_p:{"name":ad_p,"cost":ad_c,"quantity":ad_q}}}}
                    prd.update(ad_up)
                    print("Succesfully added the product")
                    input("\tPress Enter to continue")
                else:
                    print("Inavlid Input!")
                    input("\tPress Enter to continue")
            except:
                pass
        else:
            print("there is no product category name",adc)
            input("\tPress Enter to continue")
    except:
        pass
def reprt():
    print("please select product category to remove :")
    print(*prd["categories"].keys(),sep=" or ")
    adr=input("Enter category to remove :")
    if adr in prd["categories"].keys():
        print(*prd["categories"][adr].keys(),sep=" or ")
        ad_rp=input("Enter name of product to remove :")
        apme_copy={**prd["categories"]}
        for i in apme_copy.keys():
            if i==ad_rp:
                prd["categories"][adr].pop(i)
        print("Succesfully removed the product")
        input("\tPress Enter to continue")
    else:
        print(adr,"not in product list")
        input("\tPress Enter to continue")
def walar(us_w,x):
    print("Enter amount to",x,":")
    try:
        walm=int(input())
        if x=="add":
            ul[us_w]["wallet"]=ul[us_w]["wallet"]+walm
            
            print("your wallet amount is",ul[us_w]["wallet"])
            input("\tPress Enter to continue")
        else:
            ul[us_w]["wallet"]=ul[us_w]["wallet"]-walm
            print("your wallet amount is",ul[us_w]["wallet"])
            input("\tPress Enter to continue")
    except:
        pass
def wallet(us_w):
    while True:
        print(us_w,"your wallet have",ul[us_w]["wallet"],"balance")
        print("1.addamount\n2.removeamount\n3.Exit")
        us_wi=input("Enter your choice:")
        if us_wi=="1":
            walar(us_w,"add")
        elif us_wi=="2":
            walar(us_w,"sub")
        elif us_wi=="3":
            break
        else:
            print("Invalid Input!")
            input("\tPress Enter to continue")
def placeord(us_po):
    print(us_po,"enjoy")
    print("1.select product category to buy")
    print(*prd["categories"].keys(),sep=" or ")
    adc=input("Enter category to add :")
    try:
        if adc in prd["categories"].keys():
            print(*prd["categories"][adc].keys(),sep=" or ")
            ad_p=input("Enter name of product :")
            if prd["categories"][adc][ad_p]["quantity"]>0:
                for i in prd["categories"][adc][ad_p]:
                    if i!="quantity":
                        print(i,end="-->")
                        print(prd["categories"][adc][ad_p][i])
                print("Press 1 to buy the product\nPress 2 to add to cart\nPress 0 to bo back")
                uad_c=input("Enter your choice :")
                if uad_c=="1":
                    buypr(us_po,adc,ad_p)
                elif uad_c=="2":
                    cartadd(us_po,adc,ad_p)
                elif uad_c=="0":
                    pass
                else:
                    print("Invalid Input")
                    input("\tPress Enter to continue")
            else:
                print("Selected product is currently not available")
                input("\tPress Enter to continue")
        else:
            print("there is no product category name",adc)
            input("\tPress Enter to continue")
    except:
        pass
def cart(us):
    print("inside cart")
    co_u=0
    for i in ul[us]["cart"].keys():
        co_u=co_u+1
        print("\tOrder -->",co_u)
        print(i)
        for j in ul[us]["cart"][i].keys():
            print(j,end="-->")
            print(ul[us]["cart"][i][j])
        input("\tPress Enter to continue")
def newuser():
    print("Enter username:")
    nus=input()
    print("Enter password:")
    nusp=input()
    if nus not in ul:
        ulad={nus:{"password":nusp,"wallet":0,"cart":{}}}
        ul.update(ulad)
        print("user",nus,"added succesfully")
        input("\tPress Enter to continue")
    else:
        print("Please! change username and try again")
        input("\tPress Enter to continue")
def existuser():
    print("Enter your username:")
    us=input()
    print("Enter your password:")
    uspas=input()
    if ul[us]["password"]==uspas:
        print("\t",us,"Succesfully logged in")
        while True:
            print("1.wallet\n2.placeorder\n3.cart\n4.previous order\n5.Exit")
            us_int=input("Enter your choice:")
            if us_int=="1":
                wallet(us)
            elif us_int=="2":
                placeord(us)
            elif us_int=="3":
                cart(us)
            elif us_int=="4":
                prevord(us)
            elif us_int=="5":
                break
            else:
                print("Invalid Input!")
                input("\tPress Enter to continue")
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
            print("your request is in progress")
            
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
                        try:
                            print("1.Add products\n2.Remove products\n3.Exit")
                            mech=int(input("Enter your Choice :"))
                            if mech==1:
                                adprt()
                            elif mech==2:
                                reprt()
                            elif mech==3:
                                break
                            else:
                                print("Invalid Input")
                        except:
                            pass
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
            print("Invalid Input")
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
    try:
        if adl[ad]["password"]==adpas:
            print(ad,"Succesfully logged in")
            while True:
                print("1.Approve merchants\n2.Remove merchants\n3.Exit")
                adch=int(input("Enter your Choice :"))
                if adch==1:
                    approvemerch()
                elif adch==2:
                    removemer()
                elif adch==3:
                    break
                else:
                    print("Invalid Input")
        else:
            print("Invalid Login credentials")
            input("\tPress Enter to continue")
    except:
        pass 
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
            os.system("cls")
            print("New user requesting")
            newuser()
        elif us_i=="2":
            os.system("cls")
            print("Existing user login")
            existuser()
        elif us_i=="3":
            break
        else:
            print("Invalid input")
            input("\tpress enterto continue")

while True:
    os.system("cls")
    print("\tWelcome to Amazon")
    print("1.Admin\n2.Merchant\n3.User\n4.exit")
    print("Enter your choice")
    a=input()
    if a=="1":
        os.system("cls")
        print("\tAdmin login")
        admin()
    elif a=="2":
        os.system("cls")
        print("\tMerchant login")
        merchant()
    elif a=="3":
        os.system("cls")
        print("\tUser login")
        user()
    elif a=="4":
        break
    else:
        os.system("cls")
        print("Invalid Input")
