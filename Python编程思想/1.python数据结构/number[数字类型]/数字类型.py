'''
分类：
    整数、浮点数、复数
'''
'''
    整数：Python可以处理任意大小的整数，当然包括负整数，在程序中的表示和数学的写法一样
'''

num1 = 10
print(id(num1))
num1 = 20
print(id(num1))
#可以看出地址不同,可以看出python的变量的赋值实际上是，右边是先分配一个地址：数据，左边将数据的地址赋值给了标识符

num2 = num1


#连续定义多个变量
num3 = num4 = num5 = 10
print(id(num3))
print(id(num4))
print(id(num5))
#可以看出地址相同


print(num3, num4, num5)


#交互式赋值定义变量
num6, num7 = 6, 7

'''
浮点数：浮点型由整数部分与小数部分组成，浮点数运算可能会有四舍五入的误差
'''
f1 = 1.1
f2 = 2.2
print(f1 + f2)

'''
复数：实数部分和虚数部分构成，可以用a+b
'''

'''
数字类型转换
'''
#浮点型转换为整数型
print("浮点数转整数：", int(1.9))#获取整数部分

print("整数转浮点数：", float(1))#转单精浮点数

print("字符串转整数：", int("123"))

print("字符串转浮点数：", float("12.3"))


'''
print("字符串转整数：",int("abc"))
print("字符串转整数：",int("123abc"))
会报错，因为在转换类型时必须要有正确的接受转换类型
'''

print("有正负号在前面也可以正确的接受：",int("+123"))
print("有正负号在前面也可以正确的接受：",int("-123"))

'''
print(int("12+3"))
加号和减号是不能进行转换的

'''















