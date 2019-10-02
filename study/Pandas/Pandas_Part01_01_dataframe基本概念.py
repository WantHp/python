import numpy as np
import pandas as pd

# Dataframe 数据结构
# Dataframe是一个表格型的数据结构，“带有标签的二维数组”。
# Dataframe带有index（行标签）和columns（列标签）

data = {'name':['Jack','Tom','Mary'],
        'age':[18,19,20],
       'gender':['m','m','w']}
frame = pd.DataFrame(data)
print(frame)
print(type(frame))
print(frame.index,'\n该数据类型为：',type(frame.index))
print(frame.columns,'\n该数据类型为：',type(frame.columns))
print(frame.values,'\n该数据类型为：',type(frame.values))
# 查看数据，数据类型为dataframe
# .index查看行标签
# .columns查看列标签
# .values查看值，数据类型为ndarray

# Dataframe 创建方法一：由数组/list组成的字典
# 创建方法:pandas.Dataframe()

data1 = {'a':[1,2,3],
        'b':[3,4,5],
        'c':[5,6,7]}
data2 = {'one':np.random.rand(3),
        'two':np.random.rand(3)}   # 这里如果尝试  'two':np.random.rand(4) 会怎么样？
print(data1)
print(data2)
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print(df2)
# 由数组/list组成的字典 创建Dataframe，columns为字典key，index为默认数字标签
# 字典的值的长度必须保持一致！

df1 = pd.DataFrame(data1, columns = ['b','c','a','d'])
print(df1)
df1 = pd.DataFrame(data1, columns = ['b','c'])
print(df1)
# columns参数：可以重新指定列的顺序，格式为list，如果现有数据中没有该列（比如'd'），则产生NaN值
# 如果columns重新指定时候，列的数量可以少于原数据

df2 = pd.DataFrame(data2, index = ['f1','f2','f3'])  # 这里如果尝试  index = ['f1','f2','f3','f4'] 会怎么样？
print(df2)
# index参数：重新定义index，格式为list，长度必须保持一致


# Dataframe 创建方法二：由Series组成的字典

data1 = {'one':pd.Series(np.random.rand(2)),
        'two':pd.Series(np.random.rand(3))}  # 没有设置index的Series
data2 = {'one':pd.Series(np.random.rand(2), index = ['a','b']),
        'two':pd.Series(np.random.rand(3),index = ['a','b','c'])}  # 设置了index的Series
print(data1)
print(data2)
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print(df2)
# 由Seris组成的字典 创建Dataframe，columns为字典key，index为Series的标签（如果Series没有指定标签，则是默认数字标签）
# Series可以长度不一样，生成的Dataframe会出现NaN值

# Dataframe 创建方法三：通过二维数组直接创建

ar = np.random.rand(9).reshape(3,3)
print(ar)
df1 = pd.DataFrame(ar)
df2 = pd.DataFrame(ar, index = ['a', 'b', 'c'], columns = ['one','two','three'])  # 可以尝试一下index或columns长度不等于已有数组的情况
print(df1)
print(df2)
# 通过二维数组直接创建Dataframe，得到一样形状的结果数据，如果不指定index和columns，两者均返回默认数字格式
# index和colunms指定长度与原数组保持一致


# Dataframe 创建方法四：由字典组成的列表

data = [{'one': 1, 'two': 2}, {'one': 5, 'two': 10, 'three': 20}]
print(data)
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data, index = ['a','b'])
df3 = pd.DataFrame(data, columns = ['one','two'])
print(df1)
print(df2)
print(df3)
# 由字典组成的列表创建Dataframe，columns为字典的key，index不做指定则为默认数组标签
# colunms和index参数分别重新指定相应列及行标签

# Dataframe 创建方法五：由字典组成的字典

data = {'Jack':{'math':90,'english':89,'art':78},
       'Marry':{'math':82,'english':95,'art':92},
       'Tom':{'math':78,'english':67}}
df1 = pd.DataFrame(data)
print(df1)
# 由字典组成的字典创建Dataframe，columns为字典的key，index为子字典的key

df2 = pd.DataFrame(data, columns = ['Jack','Tom','Bob'])
df3 = pd.DataFrame(data, index = ['a','b','c'])
print(df2)
print(df3)
# columns参数可以增加和减少现有列，如出现新的列，值为NaN
# index在这里和之前不同，并不能改变原有index，如果指向新的标签，值为NaN （非常重要！）