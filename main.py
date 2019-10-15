times = 1
while (times < 10):
    if (times % 2 == 0):
        print(times, " times is a even number")
    else:
        print(times, " times is a odd number")
    times += 1

for letter in 'Python':  # 第一个实例
    print('当前字母 :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前水果 :', fruit)

# 迭代 a-b之间的所有的质数
# 质数：只能被自身和1整除的数字
a = 10
b = 20
for num in range(a, b + 1):
    for i in range(2, num):
        if num % i == 0:  # 如果可以被整除
            j = num / i
            print(num, "=", i, "*", int(j), ",", num, "不是质数")
            break;
    else:
        print(num, "是质数")

# 找出排序数组的索引
# def deduplication(self, nums):
#
#     for i in range(len(nums)):
#         if nums[i]==self:
#             return i
#     i=0
#
#     for x in nums:
#         if self>x:
#             i+=1
#
#     return i
#
# print(deduplication(5, [1,3,5,6]))

var1 = 5
var2 = 6
print(var1, var2)
# del var1
print(complex(2, 1))
print(abs(-5))

import cmath, math, random

dir(cmath)
print("# round 五舍六入")
print(math.ceil(3.4))
print(math.floor(3.4))
print(math.exp(1))
print(math.fabs(10))
print(int(math.pow(3, 2)))
# round 五舍六入
print(round(4.6))
print(round(4.5))
print(round(random.random(), 2))
print("---------list/append/shuffle/sort-----------")
list0 = [10, 11, 18, 99, 66, 32, 39]
print("最小数", min(list0))
print("最大数", max(list0))
list0.append('*.py')
print(list0[-1])
print("长度", len(list0))
random.shuffle(list0)
print(list0)
print(random.uniform(3, 8))
print("-----------------------")
print(math.tan(45))
print(math.sin(math.pi / 6))

print("-----------------------")
print((math.pi / 6))
print((math.pi))
print(math.sin(math.pi / 6))
print(math.sin(3.14 / 6))
print(math.log(27, 3))
print("---------tri --------")
print(round(math.sin(math.pi / 6), 2))
print(math.sin(math.pi / 6))

print(math.cos(30))

str1 = "Hello,Python"
print(str1[0: 5])
print(str1[11])

print("My name is %s and weight is %d kg!" % ('Zara', 21))

print("--------Collection---list----------")
list2 = [12, 12, 434, 66, 3221, 13, 13, 12, 13, 11, 12, 12, 'asdf', 'asdf']
print(list2.count(12))
print(list2.index('asdf'))
print("------deal the exception--------")
try:
    print(list2.index(32211))
except Exception as ex:
    print("--A exception occurred now !!!")
    print('The Exception is "' + str(ex) + '"')
else:
    print("--else其他执行了")
finally:
    print("--finally最后执行了")

print("----------display the Excetion raised by accident----------")

# raise NameError('HiThere')
# Traceback (most recent call last):

try:
    raise KeyboardInterrupt
except KeyboardInterrupt as kbint:
    print(kbint)
finally:
    print("The User take a KeyBoardInterrupt Action to occur the exception.")
    pass


print("--------tumple--------")
tup1 = (1,2,3,4)
tup2 = 'a','b','c','d',0
tup0 = ()
tup4 = tup2 + tup1
print(tup1,tup2,tup0)
print(tup4)
tup5 = tuple(list2)
print(tup5,"the tumple length is",len(tup5))

print("------------python dictionary-----list of map--------")
dic1 = {'a':1,'b':3}
# key is unique,the same key would replaced with the last one
dic2 = {'a':1,'b':3,'b':2222,3:'third elem'}
print(dic1,dic2)
print(dic2['a'])
print(dic2[3])

print("--------time module--------")
import time
print(time.localtime())
ticks = time.time()
print(ticks)
localTime = time.localtime(ticks)
print(localTime)
localTimeInFormat = time.asctime()
print("time.asctime():",localTimeInFormat)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
print(time.mktime(time.strptime(time.asctime(),"%a %b %d %H:%M:%S %Y")))


print("--------calender module--------")
import calendar
cal = calendar.month(2019,10)
print(cal)

print("--------def the funciton----------")

def printTime(str1):
    str0 = "abc"
    print(str0,"-",str1)
    return (str0+str1);

print(printTime('def'))

def changeInt(intVal):
    intVal +=1

def changeList(listValue):
    listValue.append('4')
print("immutable param in fucntion: basic data type, string, tumple")
intVal0 = 2;
changeInt(intVal0)
print(intVal0)
print("mutable param in fucntion:Dictionary{?:?, ?:?, ?:?},List")
listValue = [1,2,3]
changeList(listValue)
print(listValue)

print("----------default param value----------------")
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print("Name: ", name)
   print("Age ", age)
   return ;

def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print("输出: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return;

printinfo(70,88,99)
print("---lambda expression---")
summary = lambda p1,p2,p3: p1+p2-p3
print(summary(10, 4, 5))

print("------indencing the printShape.py edited customly------")
# import printShape

sum = 0
n0 = 0
x =1
while True:
    if n0>20:
        break
    else:
        n0 += 1
        sum = sum + x
        x = 2 ** n0
    print(sum)

print('-----------file operation----------')

jdbcType = open('C:\\Users\Administrator\Desktop\jdbcType-javaType - Copy.txt',mode='a+',encoding='utf-8')

print('File-Encoding:',jdbcType.encoding)
print('Open-Mode:',jdbcType.mode)
print('Readable:',jdbcType.readable())
print('Writable:',jdbcType.writable())
print('FileName:',jdbcType.name)
print('FileSize(unit:Byte):',jdbcType.tell())

jdbcType.write('\nPython    WrittenWords')
# print(jdbcType.read())

# 准备读取第一行
print(jdbcType.readline(),end='')
# 已经读完第一行了
print(jdbcType.readline(),end='')
# 每行都读出来
fileLine = jdbcType.readlines()
for line in fileLine:
    print(line,end='')
# 刷新缓冲，写入
jdbcType.flush()
# 关闭管道
jdbcType.close()















