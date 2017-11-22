# +(加)
print(2 + 3)

print('a' + 'b')

# *(乘)
# 给出两个数的乘积,或返回字符串重复指定次数后的结果。
print('la' * 3)

# /	除
print(4 / 3)
# //	取整除	返回商的整数部分
print(4 // 3.0)

# %	取模	返回除法的余数
print(8 % 3)
print(-25.5 % 2.25)
# <<	左移	把一个数的比特向左移一定数目（每个数在内存中都表示为比特或二进制数字，即0和1）	2 << 2得到8。——2按比特表示为10
print(2 << 2)
# >>	右移	把一个数的比特向右移一定数目	11 >> 1得到5。——11按比特表示为1011，向右移动1比特后得到101，即十进制的5。
print(11 >> 1)
# &	按位与	数的按位与	5 & 3得到1。
print(5 & 3)
# |	按位或	数的按位或	5 | 3得到7。
print(5 | 3)
# ^	按位异或	数的按位异或	5 ^ 3得到6
print(5 ^ 3)
# ~	按位翻转	x的按位翻转是-(x+1)
print(~1)
# not	布尔“非”	如果x为True，返回False。如果x为False，它返回True。	x = True; not x返回False。
print(not True)
# and	布尔“与”	如果x为False，x and y返回False，否则它返回y的计算值。
# x = False; y = True; x and y，由于x是False，返回False。
# 在这里，Python不会计算y，因为它知道这个表达式的值肯定是False（因为x是False）。这个现象称为短路计算。
print(True and False)
# or	布尔“或”	如果x是True，它返回True，否则它返回y的计算值。
# x = True; y = False; x or y返回True。短路计算在这里也适用。
print(True or False)

length = 5
breadth = 2
area = length * breadth
print('Area is', area)
print('Perimeter is', 2 * (length + breadth))
