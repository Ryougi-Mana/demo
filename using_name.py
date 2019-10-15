#!/usr/bin/python3
# Filename: using_name.py

import cmath

if __name__ == '__main__':
   print('程序自身在运行')
   print('这个属性是：', __name__)
else:
   print('我来自另一模块')
   print('这个属性是：',__name__)