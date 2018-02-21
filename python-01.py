#
#元组-不可更改的数据序列，使用圆括号进行表示
a = (1,'hello')
#通过索引进行访问
print(a[1])
#报错：TypeError: 'tuple' object does not support item assignment
#a[1] = 'world'


#列表-可以更改的数据序列（不仅可以更改列表中的元素，还可以在列表中新增元素）
b = [1,'hello']
print(b[0])
#可以重新对列表中的元素赋值
b[0] = 'world'
print(b[0])


#字典-以名称索引的分组数据
c = {'breakfast':'eggs','launch':'rice','':'noodles'}
print(c.get('launch'))


#集合-不包括重复数据的数据集(可变集合和不可变集合) (待定)

