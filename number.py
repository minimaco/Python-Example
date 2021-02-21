# 导入库
import math
import random

'''
分类：整数、浮点数、复数
'''

'''
整数： Python可以处理任意大小的整数,同时也包括负整数，在程序表达方式与数学写法一样
'''
num1 = 10
num2 = num1

# 当然也可以连续定义变量赋予同样的值
num3 = num4 = num5 = 1
print(num3, num4, num5)

# 交互式定义变量
num6, num7 = 6, 7
print(num6, num7)

'''
浮点数：由整数和小数组成，运算过程中会有四舍五入的误差
'''
f1 = 1.1
f2 = 2.2
print(f1 + f2)

'''
复数： 由实数与虚数组成
'''
'''
数字类型转换
'''
print(int(1.1))
print(int(1.9))
print(float(1.9))
print(float(1))

# 键入正负号
print(int("-123"))
print(int("+123"))

# 求绝对值
num8 = -10
print(abs(num8))
num9 = abs(num8)
print(num9)

# 数值比较
print(max(1, 2, 3, 4, 5))
print(min(1, 2, 3, 4, 5))

#计算2^5
print(pow(2, 5))

# 求整数
print(round(4.5))
print(round(4.6))
# 保留小数位置，保留2位 round(x, y) round(2.34, 1)
print(round(2.345, 2))

# 向上取整
print(math.ceil(18.1))
print(math.ceil(18.9))
# 向下取整
print(math.floor(18.1))
# 分开打印小数与整数
print(math.modf(22.3))

# 随机数
print(random.choice([1, 2, 454, 243, 21, 54]))
print(random.choice(range(5))) # 5 == [0,1,2,3,4]
# Maco == ["M", "a", "c", "o"]
print(random.choice("Maco"))

# 如果结尾不 + 1，那么默认是从0开始9结尾，如果 + 1那么输出的随机数字是从1开始的自然数
R1 = random.choice(range(10)) + 1
print(R1)
# 从1开始到100结尾，但不包含100的数字，步长是2的随机的数字，2代表随机数字需要"+2"输出，输出为奇数
print(random.randrange(1, 100, 2))

# 生成随机数字范围是[0,1)
print(random.random())

# 将list中的值随机排序
list = [1, 2, 3, 4, 5]
random.shuffle(list)
print(list)

# 随机生成一个实数，范围是[3,5]
print(random.uniform(3, 5))
