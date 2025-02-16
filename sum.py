class Adding:
    def __init__(self):
        self.arr = list(map(int, input("Enter the values to be added (space-separated): ").split()))
        self.user = input('Enter the method new or old (n or o)').lower()
        self.choice()

    def sum1(self):
        temp = 0
        for i in self.arr:
            temp += i
        print("Sum using loop:", temp)

    def sum2(self):
        print("Sum using sum():", sum(self.arr))

    def choice(self):
        if self.user=='n':
            self.sum2()
        elif self.user=='o':
            self.sum1()
        else:
            print('invalid input, choose value (n or o)')
Adding()

