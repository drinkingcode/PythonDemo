#对真假值取反
print(not True)   #False


#if-else
a = 3
b = 5
if a>b:
    print('a > b')
elif a<b:
    print('a < b')
else:
    print('a = b')


#循环
#while...:
#for...in...:
i = 0
while i<10:
    print('while-i: ' + str(i))  #打印0-9
    i = i + 1


for i in range(0,10,1):          #这里的range是python中的一个函数
    print('for-in-i: ' + str(i))   #打印0-9



#错误处理 (待定)
try:
    a = 10
    b = 0
    c = a/b
except:
    print('this is an error')

