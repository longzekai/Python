# import 与 from...import
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *
# import sys
#
# print('================Python import mode==========================');
# print('命令行参数为:')
# for i in sys.argv:
#     print(i)
# print('\n python path is', sys.path)

# 导入sys模块的argv, path成员
from sys import argv, path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path


i = 5
print(i)

i = i + 1
print(i)

s = '''This is a multi-line string.
This is the second line.'''
print(s)
# 不建议使用分号
# a = 8; print(a);
print()

s = 'This is a string. \
This continues the string.'
print(s)

i = 5
# 下面将发生错误,注意行首有一个空格
# print('Value is',i)
print('I repeat, the value is', i)

# 等待用户输入
# input('\n\n按下 enter 键后退出。')
