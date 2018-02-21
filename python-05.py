#文件操作

#读取文件
file_path = './module/animal.py'
with open(file_path) as file_object:
    file_content = file_object.read()
    print(file_content)


#写入文件
filename = 'test.txt'
with open(filename,'w') as file_object:
    file_object.write('hello world!')


#更深入的学习，可参考官网：https://docs.python.org/3/library/
