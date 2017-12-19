# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
print('========元组=========')
tup5 = ('Google', 'bitshares', '2017', '1219')
tup2 = (1, 2, 3, 4)
tup3 = 'a', 'b', 'c', 'd'
print(tup5)
print(tup2)
print(tup3)

# 创建空元组
print('========创建空元组=========')
tup4 = ()
print(tup4)
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
print('========只包含一个元素=========')
tup1 = (50)  # 不加逗号，类型为整型
print(type(tup1))

tup1 = (50,)  # 加上逗号，类型为元组
print(type(tup1))
# 元组与字符串类似，下标索引从0开始，可以进行截取，组合等。
print('========访问元组=========')
print('tup5[0]:', tup5[0])
print('tup2[1:3]:', tup2[1:3])
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
print('========修改元组=========')
tup6 = (12, 34.56)
tup7 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup6[0] = 100
# 创建一个新的元组
tup8 = tup6 + tup7
print(tup8)

# 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
print('========删除元组=========')
print(tup5)
del tup5
print("删除后的元组 tup : ")
# print(tup5)
# 元组运算符
# 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。
# 这就意味着他们可以组合和复制，运算后会生成一个新的元组。
print('========元组运算符=========')
print(len(tup8))
print(('Hi!',) * 4)
print((12 in tup8))
for x in tup2:
    print(x)

# 元组索引，截取
# 因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素
print('========元组运算符=========')
print(tup8[2])
print(tup8[-2])
print(tup8[1:])

# 元组内置函数
# Python元组包含了以下内置函数
# 序号	方法及描述	实例
# 1	len(tuple)
# 计算元组元素个数。
# >>> tuple1 = ('Google', 'Runoob', 'Taobao')
# >>> len(tuple1)
# 3
# >>>
# 2	max(tuple)
# 返回元组中元素最大值。
# >>> tuple2 = ('5', '4', '8')
# >>> max(tuple2)
# '8'
# >>>
# 3	min(tuple)
# 返回元组中元素最小值。
# >>> tuple2 = ('5', '4', '8')
# >>> min(tuple2)
# '4'
# >>>
# 4	tuple(seq)
# 将列表转换为元组。
# >>> list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
# >>> tuple1=tuple(list1)
# >>> tuple1
# ('Google', 'Taobao', 'Runoob', 'Baidu')
print('========元组内置函数=========')
print(max(tup2))
print(min(tup2))
list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1 = tuple(list1)
print(tuple1)
