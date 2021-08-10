import random
#game start
gs=""
asp=1
hs=0
ok=input("User what was your name? ")
print(ok)
while True:    
    while gs.lower() != "start":
        print("if you error 3 times the game will over")
        gs=input("Type \"START\" to start the math game: ")
        if gs.lower() != "start":
            print(gs)
    #questions maker and printer
    en=0
    sc=0
    print("Game started!")
    while en != 3:
        loo=random.randint(2,10)
        lot=random.randint(2,10)
        print("Question "+str(asp))
        rs=loo*lot
        sda=input(str(loo)+" x "+str(lot)+" = ")
        print(sda)
        if int(sda) == rs:
            print("Congratulations "+ok+", The Question "+str(asp)+" its correct")
            sc=sc+1
            asp=asp+1
        else:
            print("Good Luck in the next time "+ok+", The awser its "+str(rs))
            en=en+1
            asp=asp+1
    if sc > hs:
        hs=sc
    print(ok+" the game over, you score "+str(sc)+", and you highscore is "+str(hs))
    asp=1
#trick
while True:
    pass
