import random
def game_1():
    print("==============")
    print("ROCK PAPER SCISSORS GAME")
    print("==============")
    s=0
    s1=0
    c=1
    while(True):
        L=["rock","paper","scissors"]
        n=input("Enter :")
        n1=random.choice(L)
        if n.isalpha()==True and n.lowe() in L:
            if n.lower()==n1:
                print("***********")
                print("TIE")
                if c==5:
                    break    
            elif ( n.lower()=="rock" and n1=="paper") or (n.lower()=="Paper" and n1=="scissors") or (n.lower()=="scissors" and n1=="rock"):
                print("***********")
                print("COMPUTER WIN")
                s1=s1+1
                if c==5:
                    break 
            elif ( n.lower()=="paper" and n1=="rock") or (n.lower()=="scissors" and n1=="paper") or (n.lower()=="rock" and n1=="scissors"):
                print("**********")
                print("YOU WIN")
                s=s+1
                if c==5:
                    break
            c+=1   
        else:
            print("************")
            print("ENTER VALID ALPHABET ")

    if s>s1:
        print("===================")
        print("You Win / Your Point Is",s)
    elif s<s1:
        print("===================")
        print("You Loss/ Your Point Is",s)
    else:
        print("===================")
        print("Tie")
game_1()
