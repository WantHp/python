import numpy as np

#基本索引以及切片


ar = np.arange(20)
print(ar)
print(ar[4])
print(ar[3:6])
print('-----')
# 一维数组索引及切片

ar = np.arange(16).reshape(4,4)
print(ar, '数组轴数为%i' %ar.ndim)   # 4*4的数组
print(ar[2],  '数组轴数为%i' %ar[2].ndim)  # 切片为下一维度的一个元素，所以是一维数组
print(ar[2][1]) # 二次索引，得到一维数组中的一个值
print(ar[1:3],  '数组轴数为%i' %ar[1:3].ndim)  # 切片为两个一维数组组成的二维数组
print(ar[2,2])  # 切片数组中的第三行第三列 → 10
print(ar[:2,1:])  # 切片数组中的1,2行、2,3,4列 → 二维数组
print('-----')
# 二维数组索引及切片

ar = np.arange(8).reshape(2,2,2)
print(ar, '数组轴数为%i' %ar.ndim)   # 2*2*2的数组
print(ar[0],  '数组轴数为%i' %ar[0].ndim)  # 三维数组的下一个维度的第一个元素 → 一个二维数组
print(ar[0][0],  '数组轴数为%i' %ar[0][0].ndim)  # 三维数组的下一个维度的第一个元素下的第一个元素 → 一个一维数组
print(ar[0][0][1],  '数组轴数为%i' %ar[0][0][1].ndim)
# **三维数组索引及切片


# 数组索引及切片的值更改、复制

ar = np.arange(10)
print(ar)
ar[5] = 100
ar[7:9] = 200
print(ar)
# 一个标量赋值给一个索引/切片时，会自动改变/传播原始数组

ar = np.arange(10)
b = ar.copy()
b[7:9] = 200
print(ar)
print(b)
# 复制


# 布尔型索引及切片

ar = np.arange(12).reshape(3,4)
i = np.array([True,False,True])
j = np.array([True,True,False,False])
print(ar)
print(i)
print(j)
print(ar[i,:])  # 在第一维度做判断，只保留True，这里第一维度就是行，ar[i,:] = ar[i]（简单书写格式）
print(ar[:,j])  # 在第二维度做判断，这里如果ar[:,i]会有警告，因为i是3个元素，而ar在列上有4个
# 布尔型索引：以布尔型的矩阵去做筛选

m = ar > 5
print(m)  # 这里m是一个判断矩阵
print(ar[m])  # 用m判断矩阵去筛选ar数组中>5的元素 → 重点！后面的pandas判断方式原理就来自此处