account=100000
card="c"
pwd=1234
while True:
    card=input("INSERT THE CARD:")
    if card=="c":
        print("WELCOME AMRUTHA")
        p=int(input("enter the password:"))
        if p==pwd:
            choice=int(input("OPTIONS:1.BALANCE ENQUIRY,OPTION:2.WITHDRAW"))
            if choice==2:
                w=int(input("enter the withdraw money:"))
                print(f"account balance:{account-w}")
            else:
                print(f"account balance:{account}")

        else:
            print("incorrect password")
    else:
        print("invalid card")
            
