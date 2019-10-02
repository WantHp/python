import numpy as np
import os as os

print(os.getcwd())

ar=np.random.rand(5,5)
print(ar)

np.save('data/arraydata',ar)

ar_load=np.load('data/arraydata.npy')

print(ar_load)

# 存储/读取文本文件

ar = np.random.rand(5,5)
np.savetxt('data/array.txt',ar, delimiter=',')
# np.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')：存储为文本txt文件

ar_loadtxt = np.loadtxt('data/array.txt', delimiter=',')
print(ar_loadtxt)
# 也可以直接 np.loadtxt('C:/Users/Hjx/Desktop/array.txt')
