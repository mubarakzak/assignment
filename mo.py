balance=897.32
print("    MTN MOMO   ")
print("""
1)        check Balance       
2)        transfwe
3)        deposit


""")
Option=int(input("Enter Option: "))

if Option==1:
    pin = int(input('enter pin: ')) 
    print(balance)

if Option==2:
    pin = int(input('enter pin: '))    
    transfer=float(input("Enter recipient number "))
    transfer=float(input("Enter transfer amount  "))
    if transfer>0:
        forewardbalance=(balance-transfer)
        print("Foreward Balance  Â£ ",forewardbalance)
    elif transfer>balance:
        print("No funs in account")
    else:
        print("None withdraw made")

if Option==3:
    pin = int(input('enter pin: ')) 
    Deposit=float(input("Enter deposit amount Â£ "))
    if Deposit>0:
        forewardbalance=(balance+Deposit)
        print("Forewardbalance  Â£ ",forewardbalance)
    else:
        print("None deposit made")


