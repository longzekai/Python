# 多个变量赋值
# Python允许你同时为多个变量赋值。例如：
a = b = c = 1
print(a, b, c)

# 您也可以为多个对象指定多个变量。例如：
a, b, c = 1, 2, "Danny"
print(a, b, c)

# Number
# Python3 支持 int、float、bool、complex（复数）。
# 在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# 像大多数语言一样，数值类型的赋值和计算都是很直观的。
# 内置的 type() 函数可以用来查询变量所指的对象类型。
# Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示，
# 复数的实部a和虚部b都是浮点型
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

# 还可以用 isinstance 来判断：
a = 111
print(isinstance(a, int))

# 区别就是:
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
# class A:
#     print('A')
# class B(A):
#     print('B')
# isinstance(A(), A)  # returns True
# type(A()) == A      # returns True
# isinstance(B(), A)    # returns True
# type(B()) == A        # returns False

# String
# 字符串的截取的语法格式如下：
# 变量[头下标:尾下标]
# 索引值以 0 为开始值，-1 为从末尾的开始位置。
# 加号 (+) 是字符串的连接符， 星号 (*) 表示复制当前字符串，紧跟的数字为复制的次数
print('==========String============')
str = 'Runoob'
print('1:', str)  # 输出字符串
print('2:', str[0:-1])  # 输出第一个到倒数第二个的所有字符
print('3:', str[0])  # 输出字符串第一个字符
print('4:', str[2:5])  # 输出从第三个开始到第五个的字符
print('5:', str[2:])  # 输出从第三个开始的后的所有字符
print('6:', str * 2)  # 输出字符串两次
print('7:', str + "TEST")  # 连接字符串
print('8:', str[-1])

# List 列表
# 列表截取的语法格式如下：
# 变量[头下标:尾下标]
# 索引值以 0 为开始值，-1 为从末尾的开始位置。
# 加号（+）是列表连接运算符，星号（*）是重复操作。
list = ['abcd', 786, 2.23, 'danny', 70.2]
tinyList = [123, 'danny']
print('==========list============')
print('1:', list)
print('2:', list[0])
print('3:', list[1:3])
print('4:', list[2:])
print('5:', tinyList * 2)
print('6:', list + tinyList)

# 列表中的元素是可以改变的
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)

# Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同：
print('==========tuple============')
tuple = ('abcd', 786, 2.23, 'danny', 70.2)
tinytuple = (123, 'zhou')
print('1:', tuple)
print('2:', tuple[0])
print('3:', tuple[1:3])
print('4:', tuple[2:])
print('5:', tinyList * 2)
print('6:', tuple + tinytuple)

# 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。
# 其实，可以把字符串看作一种特殊的元组。
print('==========tuple2============')
tup = (1, 2, 3, 4, 5, 6)
print(tup[0])
print(tup[1:5])
# tup[0] = 11  # 修改元组元素的操作是非法的

# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
print('==========tuple3============')
tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号
print(tup1)
print(tup2)
# string、list和tuple都属于sequence（序列）。
# 1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法一样。
# 3、注意构造包含0或1个元素的元组的特殊语法规则。
# 4、元组也可以使用+操作符进行拼接。
print('==========tuple end============')

print('==========Set Start============')
# Set（集合）
# 集合（set）是一个无序不重复元素的序列。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，
# 因为 { } 是用来创建一个空字典。
# 创建格式：
# parame = {value01,value02,...}
# 或者
# set(value)
parame = {2, 3, 4, 'danny'}
print(parame)
print('parame is', type(parame))
print(set())
print(set([2, 3, 4, 5, 6, 4 + 3j]))

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素




















