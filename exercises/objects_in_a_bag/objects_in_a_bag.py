from random import shuffle

COLORS = ["transparent", "red", "green", "blue"]


class Item:

    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
        return

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def getWeight(self):
        return self.weight

    def isMyName(self, name):
        return self.name == name

    def getDescription(self):
        return "[name: " + self.getName() + ", color: " + self.getColor() + ", weight: " + str(self.getWeight()) + "]"


class Bag:

    def __init__(self, label):
        self.items = []
        self.label = label
        return

    def addItem(self, item):
        self.items.append(item)
        return

    def shuffle(self):
        shuffle(self.items)
        return

    def getItems(self):
        return self.items

    def getLabel(self):
        return self.label

    def getDescription(self):
        total = "'" + self.getLabel() + "' contains the following:\n"
        for item in self.getItems():
            total = total + " - " + item.getDescription() + "\n"
        return total


def task_program():
    command = ""
    bag = Bag("Cool bag of stuff")
    while (True):
        got = input().split(" ")
        l_got = len(got)
        if l_got > 0:
            command = got[0]
            if command == "exit":
                break
            elif command == "add":
                if l_got > 4:
                    print("Too many arguments!")
                    continue
                if l_got == 1:
                    print("Too few arguments!")
                    continue
                name = ""
                color = COLORS[0]
                weight = 0.0
                if l_got > 3:
                    try:
                        weight = float(got[3])
                    except ValueError:
                        print("Unable to parse weight.")
                        continue
                if l_got > 2:
                    try:
                        index = COLORS.index(got[2])
                        color = COLORS[index]
                    except ValueError:
                        print("Unable to parse color.")
                        continue
                name = got[1]
                item = Item(name, color, weight)
                print("Added item: " + item.getDescription())
                bag.addItem(item)
            elif command == "show":
                print(bag.getDescription())
            elif command == "shuffle":
                bag.shuffle()
                print("Shuffling the bag...")
            else:
                print("Unknown command: " + command)
        else:
            print("Unable to parse command.")


task_program()
