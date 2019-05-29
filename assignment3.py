import random
def funct():
    x=random.randint(0,20)
    f_name=input("Enter first name: ")
    l_name=input("Enter last name: ")
    ct=0
    while True:
        if ct==3:
            print("sorry program crashed")
            break
        try:
            user_input=int(input("enter number in the range of 1-20: "))
        except:
            print("enter valid number: ")
            ct=ct+1
            continue
        if user_input==x:
            print("otp matched")
            break
        elif(user_input>20):
            print("wrong input..try again")
            ct=ct+1
            continue
        else:
            print("Error enter the otp again")
            user_input2=input("press yes to continue..or no to quit: ")
        if user_input2=='yes':
            continue
        else:
            print("thanks for your attempt")
            break
funct()            





        