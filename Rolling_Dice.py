import random

class rolling_dice :
    def __init__(self):
        choice=input("choose a methode new = n, old = o : ").lower()
        if choice=='n' :
            self.new_method()
        elif choice=='o':
            self.old_method()
        else :
            print("Invalid input : Type n or o")

    def old_method (self):
        while(True):
            value=(input("Roll the dice(y/n)"))
            if(value=='y'):
                random_int1=random.randint(1,6)
                random_int2=random.randint(1,6)
                print("(",random_int1,",",random_int2,")")
            elif(value=='n'):
                print("Thaks for playing dice!")
                break
            else:
                print("invalid input!\nplease enter y or n")

    def new_method (self):
        while(True):
            value=(input("Roll the dice(y/n)"))
            if(value=='y'):
                lst=[random.randint(1,6),random.randint(1,6)]
                print(lst)
            elif(value=='n'):
                print("Thaks for playing dice!")
                break
            else:
                print("invalid input!\nplease enter y or n")

rolling_dice()
