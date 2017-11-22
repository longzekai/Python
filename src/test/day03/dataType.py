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
str = 'Runoob'
print('1:', str)  # 输出字符串
print('2:', str[0:-1])  # 输出第一个到倒数第二个的所有字符
print('3:', str[0])  # 输出字符串第一个字符
print('4:', str[2:5])  # 输出从第三个开始到第五个的字符
print('5:', str[2:])  # 输出从第三个开始的后的所有字符
print('6:', str * 2)  # 输出字符串两次
print('7:', str + "TEST")  # 连接字符串
print('8:', str[-1])
