import numpy as np
import pandas as pd

#查看数据
s=pd.Series(np.random.rand(15))
print(s.head(2))
print(s.tail(2))

#重新索引 reindex
s=pd.Series(np.random.rand(5),index=['a','b','c','d','e'])
print(s)
s1 = s.reindex(['c','b','a','f'])
print(s1)

s2 = s.reindex(['c','b','a','f'], fill_value = 0)
print(s2)


#对齐
# Series对齐

s1 = pd.Series(np.random.rand(3), index = ['Jack','Marry','Tom'])
s2 = pd.Series(np.random.rand(3), index = ['Wang','Jack','Marry'])
print(s1)
print(s2)
print(s1+s2)
# Series 和 ndarray 之间的主要区别是，Series 上的操作会根据标签自动对齐
# index顺序不会影响数值计算，以标签来计算
# 空值和任何值计算结果扔为空值

# 删除：.drop

s = pd.Series(np.random.rand(5), index = list('ngjur'))
print(s)
s1 = s.drop('n')
s2 = s.drop(['g','j'])
print(s1)
print(s2)
print(s)
# drop 删除元素之后返回副本(inplace=False)


# 添加

s1 = pd.Series(np.random.rand(5))
s2 = pd.Series(np.random.rand(5), index = list('ngjur'))
print(s1)
print(s2)
s1[5] = 100
s2['a'] = 100
print(s1)
print(s2)
print('-----')
# 直接通过下标索引/标签index添加值

s3 = s1.append(s2)
print(s3)
print(s1)
# 通过.append方法，直接添加一个数组
# .append方法生成一个新的数组，不改变之前的数组


# 修改

s = pd.Series(np.random.rand(3), index = ['a','b','c'])
print(s)
s['a'] = 100
s[['b','c']] = 200
print(s)
# 通过索引直接修改，类似序列