#create class - main
class Brik():
    def __init__(self,length,width,height):
        self.length =length
        self.width = width
        self.height = height
# create class for tall brik via inheritance
class Tall(Brik):
    def __init__(self, length, width, height):
        super().__init__(length, width, height)

    def calculate_market_value(self):
        base = self.width * self.length
        market_value = base *0.1+self.height*0.2
        return market_value
# create class for flat brik via inheritance
class Flat(Brik):
    def __init__(self, length, width, height):
        super().__init__(length, width, height)

    def calculate_market_value(self):
        market_value = self.width * self.length * 0.15
        return market_value
# create class for supafig brik via inheritance
class SupaFig(Brik):
    def __init__(self, length, width, height):
        super().__init__(length, width, height)

    def calculate_market_value(self):
        market_value = 2.85
        return market_value

# intro heading for program
print("BRIK VALUE CALCULATOR")
# function to run the program
def program():
    category = input("Enter the category of brik. (t = tall, f = flat, s = SupaFig) ") # user input which brik
    # print(category)
    if category in ['t','f','s']:
        if category == 't': # tall brik selected
            # print('tall brik selected')
            while True:
                try:
                    length = int(input("Enter the length in units: "))
                    if length >= 1:
                        break
                    else:
                        print("Unit needs to be 1 or more.")
                except ValueError:
                    print("Please enter a valid number.")
            while True:
                try:
                    width = int(input("Enter the width in units: "))
                    if width >= 1:
                        break
                    else:
                        print("Unit needs to be 1 or more.")
                except ValueError:
                    print("Please enter a valid number.")
            while True:
                try:
                    height = int(input("Enter the height in units: "))
                    if height >= 1:
                        break
                    else:
                        print("Unit needs to be 1 or more.")
                except ValueError:
                    print("Please enter a valid number.")
            # print(length,width,height)
            brik = Tall(length,width,height)
            # print(brik)
            print(f"Your brik:\nDIMENSIONS: length of {length}, width of {width}, height of {height}\nPREDICTED MARKED VALUE: ${brik.calculate_market_value():.2f}")
        elif category == 'f':# flat brik selected
            # print('flat brik selected')
            while True:
                try:
                    length = int(input("Enter the length in units: "))
                    if length >= 1:
                        break
                    else:
                        print("Unit needs to be 1 or more.")
                except ValueError:
                    print("Please enter a valid number.")
            while True:
                try:
                    width = int(input("Enter the width in units: "))
                    if width >= 1:
                        break
                    else:
                        print("Unit needs to be 1 or more.")
                except ValueError:
                    print("Please enter a valid number.")
            height = 0
            # print(length,width,height)
            brik = Flat(length,width,height)
            # print(brik)
            print(f"Your brik:\nDIMENSIONS: length of {length}, width of {width}, height of {height}\nPREDICTED MARKED VALUE: ${brik.calculate_market_value():.2f}")
        elif category == 's':# supafig brik selected
            # print('supafig brik selected')
            length = 2
            width = 1
            height = 3
            # print(length,width,height)
            brik = SupaFig(length,width,height)
            # print(brik)
            print(f"Your brik:\nDIMENSIONS: length of {length}, width of {width}, height of {height}\nPREDICTED MARKED VALUE: ${brik.calculate_market_value():.2f}")
    else: # when input is not found, it gives error
        print("Category not found")
        program()
program()



# dont worry about this
import csv
def programv2():
    categories = {}
    # category,length,width,height
    # tall,none,none,none
    # flat,none,none,0
    # SupaFig,2,1,3
    with open('sac/brik.csv','r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            categories[row[0]] = {
                "length": row[1],
                "width": row[2],
                "height": row[3]
            }
    options = ''
    for category in categories:
        options += f'{category[0]} = {category}, '
    category = input(f"Enter the category of brik. ({options}) ")
    for option in categories:
        if option[0] == category:
            print(categories[option])
            length = categories[option]['length']
            width = categories[option]['width']
            height = categories[option]['height']
            if length == 'none':
                length = int(input('Enter the length in units. '))
                while length <= 1:
                    length = int(input('Enter the length in units. '))
            if width == 'none':
                width = int(input('Enter the width in units. '))
                while width <= 1:
                    width = int(input('Enter the width in units. '))
            if width == 'none':
                width = int(input('Enter the width in units. '))
                while width <= 1:
                    width = int(input('Enter the width in units. '))

            # print(option.capitalize()(length,width,width))
# programv2()