class Lst:
    def __init__(self):
        self.lst1 = list(map(int, input("Enter an array: ").split()))

    def sort(self):
        value = int(input("Press 1 for normal sort\nPress 2 for reverse sort: "))
        if value == 1:
            self.lst1.sort()
            print("List sorted:", self.lst1)
        elif value == 2:
            self.lst1.sort(reverse=True)
            print("List sorted:", self.lst1)
        else:
            print("Incorrect input! Press 1 or 2.")

    def addvalue(self):
        value = input("Add value at the front (f), back (b), or at an index (p): ").lower()
        if value == 'f':
            valueforf = int(input("Enter value: "))
            self.lst1.insert(0, valueforf)
        elif value == 'b':
            valueforb = int(input("Enter value: "))
            self.lst1.append(valueforb)
        elif value == 'p':
            valueforp = int(input("Enter value: "))
            valueforpi = int(input("Enter the index: "))
            if 0 <= valueforpi <= len(self.lst1):
                self.lst1.insert(valueforpi, valueforp)
            else:
                print("Error! Index out of bounds!")
        else:
            print("Invalid input! Choose f, b, or p.")
        print("Updated list:", self.lst1)

    def deletevalue(self):
        value = input("Delete from front (f), back (b), or a specific index (p): ").lower()
        if value == 'f':
            if self.lst1:
                self.lst1.pop(0)
            else:
                print("List is empty!")
        elif value == 'b':
            if self.lst1:
                self.lst1.pop()
            else:
                print("List is empty!")
        elif value == 'p':
            valueforpi = int(input("Enter the index: "))
            if 0 <= valueforpi < len(self.lst1):
                self.lst1.pop(valueforpi)
            else:
                print("Error! Index out of bounds!")
        else:
            print("Invalid input! Choose f, b, or p.")
        print("Updated list:", self.lst1)

    def run(self):
        while True:
            value = int(input("Press 1 to Sort\nPress 2 to Add Values\nPress 3 to Delete Values\nPress 4 to Exit: "))
            if value == 1:
                self.sort()
            elif value == 2:
                self.addvalue()
            elif value == 3:
                self.deletevalue()
            elif value == 4:
                print("Exiting program.")
                break
            else:
                print("Invalid input! Choose 1, 2, 3, or 4.")

# Run the program
lst_obj = Lst()
lst_obj.run()