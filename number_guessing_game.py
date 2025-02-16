import random

class guessing:
    def __init__(self):
        self.guess=random.randint(1,100)
        self.function()

    def function (self):
        while True :
            try:
                 user_guess=int(input("Guess a number between 1 to 100 : "))
            except ValueError:
                print('Value Error, Please enter value between 1 to 100')

            if 1<=user_guess<=100 :
                if user_guess< self.guess :
                    print('Too Low')
                elif user_guess>self.guess :
                    print('Too High')
                else :
                    print('Congragulations you guessed a number, its : ',self.guess)
                    break
            else :
                print('Value out of bounds, Please enter value between 1 to 100')
guessing()