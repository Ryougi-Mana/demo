
print("------------------------------")
# temp = input("请输入一个数字\n")
# temp_int = int(temp)
#
# if temp_int == 8:
#     print("输入的数字是：" + str(temp_int))
# else:
#     print("输入的不是八")

print(dir())
str1 = '我来了1'
str2 = "我来了2"

a1 = 5.0
a2 = 3.0
a3 = a1/a2
a4 = 1e10
print(str1+str2)

print(a3)
print(a4)
b1 = bool(2)
b2 = bool(1)
b0 = bool(0)
b4 = bool(-1)

print(b1)
print(b2)
print(b0)
print(b4)


i1 = round(3.99)
i2 = float("434")
print(i1)
print(i2)

str = "i l u"
print(type(str))
print(type(i2))
print((isinstance(i2,float)))
print(3**3)

print(8/3)
print(8//3)

print("------fibonacci function----------")
from fibo import fib,fib2
from fibo import *
fib(100)
print(fib2(100))
# print(fib3(99))
print(fib_attr)
sum0 =1
print('sum0=',sum0)

import cmath,sys,math

for dirMember in dir():
    print(dirMember)

def __getattr__(name):
    return str2 + str1 + name
def __setattr__(name):
    str2 = name
    str1 = name

import using_name
# dir(using_name)
if __name__ != '__main__':
    print("local")
else:
    print("other")
    print(__name__)
    print(using_name.__name__)

print("--------standard input/output---------")
helloStr = 'helloPython\n'
print(repr(helloStr))
print(repr(helloStr).__repr__())







