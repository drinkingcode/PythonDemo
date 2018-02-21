#函数的定义及使用
#函数的定义
def add(num1,num2):
    sum = num1 + num2
    print('sum: ' + str(sum))
    return sum
#函数的使用
add(10,20)


#定义和使用类
#定义类
class Animal():
    #构造函数
    def __init__(self,name):
        self.name = name
    #类的方法
    def printInfo(self):
        print('the animal is ' + self.name)

#使用类
animal = Animal('cat')
animal.printInfo()


#类的继承
#继承Animal类
class Cat(Animal):
    #构造函数
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color

    #覆盖父类的方法
    def printInfo(self):
        print('the cat name is ' + self.name + ' and color is ' + self.color)

    def run(self):
        print('the cat is running')


cat = Cat('xiaoHua','black')
cat.printInfo()  #the cat name is xiaoHua and color is black
cat.run()        #the cat is running