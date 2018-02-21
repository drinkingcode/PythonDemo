#模块
#导入一个或多个模块
from module.animal import Animal,Cat

animal = Animal('animal')
cat = Cat('xiaoHua','black')

animal.printInfo()   #the name is animal
cat.printInfo()      #the name is xiaoHua and color is black


#第三方模块的安装：pip install 模块名