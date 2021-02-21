'''
运算符：由变量、常量和运算符组成的式子

算术运算符
+   -  *   /   %    **    //
加  减  乘  除  取模  求幂   取整
'''
A = 5
B = 2
print(A + B)
print(A - B)
print(A * B)
print(A / B)
print(A % B) # 取除后的余数
print(A ** B)
print(A // B)

'''
赋值运算符
赋值运算符 “=”
表达式的格式，如下
变量 = 表达式
功能：计算等号右侧的表达式的值，并赋值给等号左侧的变量
值：就是赋值结束后变量的值
'''
num1 = 2
num2 = num1 + 20
print(num2)


'''
复合运算符
+=      a+=b    ==   a = a + b
-+      a-=b    ==   a = a - b
*=      a*=b    ==   a = a * b
/=      a/=b    ==   a = a / b
%=      a%=b    ==   a = a % b
**=     a**=b   ==   a = a ** b
//=     a//=b   ==   a = a // b
'''
num1 %= num2
print(num1)



'''
if语句
格式:
语句开头空出一个tab键，如下
if 表达式:   注意冒号一定要有
    语句

逻辑：当程序执行if时，首先会计算“表达式”的值

真假定义：
假：0 0.0 '' None flase
真：除了假就是真
'''
if num1 == num2:
    num1 = True
else:
    num1 = False
    print(num1)
