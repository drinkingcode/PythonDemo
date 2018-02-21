class Animal():
    def __init__(self,name):
        self.name = name

    def printInfo(self):
        print('the name is ' + self.name)

class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color

    def printInfo(self):
        print('the name is ' + self.name + ' and color is ' + self.color)

    def run(self):
        print('it is running')