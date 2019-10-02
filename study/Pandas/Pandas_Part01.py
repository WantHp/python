import numpy as np
import pandas as pd

# Series 数据结构
# Series 是带有标签的一维数组，可以保存任何数据类型（整数，字符串，浮点数，Python对象等）,轴标签统称为索引

ar=np.random.rand(5)
s=pd.Series(ar)
print(s)
print(type(s))

print(s.index,type(s.index))
print(s.values,type(s.values))
# 核心：series相比于ndarray，是一个自带索引index的数组 → 一维数组 + 对应索引
# 所以当只看series的值的时候，就是一个ndarray
# series和ndarray较相似，索引切片功能差别不大
# series和dict相比，series更像一个有顺序的字典（dict本身不存在顺序），其索引原理与字典相似（一个用key，一个用index）


# Series 创建方法一：由字典创建，字典的key就是index，values就是values
print('------通过字典创建----')
dic={'a':1,'b':2,'c':3,'d':4}
s=pd.Series(dic)
print(s)

print('------通过数组创建---')
ar1=np.random.rand(5)
s1=pd.Series(ar1)
print(s1)

s = pd.Series(ar1, index = ['a','b','c','d','e'],dtype = np.object)
print(s)

print('------通过标量创建---')
s=pd.Series(10,index=range(4))
print(s)


# Series 名称属性：name

s1 = pd.Series(np.random.randn(5))
print(s1)
print('-----')
s2 = pd.Series(np.random.randn(5),name = 'test')
print(s2)
print(s1.name, s2.name,type(s2.name))
# name为Series的一个参数，创建一个数组的 名称
# .name方法：输出数组的名称，输出格式为str，如果没用定义输出名称，输出为None

s3 = s2.rename('hehehe')
print(s3)
print(s3.name, s2.name)
# .rename()重命名一个数组的名称，并且新指向一个数组，原数组不变

print('----------Series的索引-----')
s=pd.Series(np.random.rand(5))
print(s)
print(s[0],type(s[0]),s[0].dtype)
print(float(s[0]),type(float(s[0])))
#print(s[-1])
# 位置下标从0开始
# 输出结果为numpy.float格式，
# 可以通过float()函数转换为python float格式
# numpy.float与float占用字节不同
# s[-1]结果如何？


# 标签索引

s = pd.Series(np.random.rand(5), index = ['a','b','c','d','e'])
print(s)
print(s['a'],type(s['a']),s['a'].dtype)
# 方法类似下标索引，用[]表示，内写上index，注意index是字符串

sci = s[['a','b','e']]
print(sci,type(sci))
# 如果需要选择多个标签的值，用[[]]来表示（相当于[]中包含一个列表）
# 多标签索引结果是新的数组


# 切片索引

s1 = pd.Series(np.random.rand(5))
s2 = pd.Series(np.random.rand(5), index = ['a','b','c','d','e'])
print(s1[1:4],s1[4])
print(s2['a':'c'],s2['c'])
print(s2[0:3],s2[3])
print('-----')
# 注意：用index做切片是末端包含

print(s2[:-1])
print(s2[::2])
# 下标索引做切片，和list写法一样


# 布尔型索引

s = pd.Series(np.random.rand(3)*100)
s[4] = None  # 添加一个空值
print(s)
bs1 = s > 50
bs2 = s.isnull()
bs3 = s.notnull()
print(bs1, type(bs1), bs1.dtype)
print(bs2, type(bs2), bs2.dtype)
print(bs3, type(bs3), bs3.dtype)
print('-----')
# 数组做判断之后，返回的是一个由布尔值组成的新的数组
# .isnull() / .notnull() 判断是否为空值 (None代表空值，NaN代表有问题的数值，两个都会识别为空值)

print(s[s > 50])
print(s[bs3])
# 布尔型索引方法：用[判断条件]表示，其中判断条件可以是 一个语句，或者是 一个布尔型数组！




