# coding=utf-8
#print ('hello')
# print ("hello # world")

# print('''这是一段多行字符串。这是它的第一行。
# This is the second line.
# "What's your name?," I asked.
# He said "Bond, James Bond."
# ''')
from idlelib.multicall import r

age = 20
name = 'Swaroop'
print ('{0} was {1} years old when he wrote this book'.format(name, age))
print ('why is {0} playing with that python? '.format(name))

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:^11}'.format('Hello'))
print('{0:_^11}'.format('Hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
print('a', end='')
print('b', end='')
print()
print('a', end=' ')
print('b', end=' ')
print('c')

# 转义序列
print('This is the first line\nThis is the second line')
print("This is the first sentence. \
This is the second sentence.")
# 多行注释可用三对双引号
"""
原始字符串
如果你需要指定一些未经过特殊处理的字符串，比如转义序列，那么你需要在字符串前增加
r  或  R  来指定一个 原始（Raw） 字符串 。下面是一个例子：
"""
print(r"Newlines are indicated by \n")

