##### Mohammad Ali Mirzaei #####

def Carpet(Number) :

    from random import choice

    lst = ["🟥","🟧","🟨","🟩","🟦","🟪","🟫"]
    if Number % 2 != 0 :

        for i in range(Number) :
            for j in range(Number) :
                if j % 2 == 0: 
                    ch = choice(lst)
                    print(ch,end="")
                else: 
                    ch = choice(lst)
                    print(ch,end="") 
            print()
    else:
        print("If you want a wonderful carept, you should enter an odd number")
             
while True : Carpet(int(input("Enter a number : ")))
