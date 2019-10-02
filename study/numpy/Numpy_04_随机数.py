import numpy as np
import matplotlib.pyplot as plt
#% matplotlib inline
# 魔法函数，每次运行自动生成图表

samples=np.random.normal(size=(4,4))
print(samples)


samples1 = np.random.rand(1000)
samples2 = np.random.rand(1000)

plt.scatter(samples1,samples2)


samples3 = np.random.randn(1000)
samples4 = np.random.randn(1000)
plt.scatter(samples3,samples4)

random_image = np.random.random([500, 500])
print(random_image)
plt.imshow(random_image, cmap='gray')
plt.colorbar()
plt.show()

# numpy.random.randint(low, high=None, size=None, dtype='l')：生成一个整数或N维整数数组
# 若high不为None时，取[low,high)之间随机整数，否则取值[0,low)之间随机整数，且high必须大于low
# dtype参数：只能是int类型

print(np.random.randint(2))
# low=2：生成1个[0,2)之间随机整数

print(np.random.randint(2,size=5))
# low=2,size=5 ：生成5个[0,2)之间随机整数

print(np.random.randint(2,6,size=5))
# low=2,high=6,size=5：生成5个[2,6)之间随机整数

print(np.random.randint(2,size=(2,3)))
# low=2,size=(2,3)：生成一个2x3整数数组,取数范围：[0,2)随机整数

print(np.random.randint(2,6,(2,3)))
# low=2,high=6,size=(2,3)：生成一个2*3整数数组,取值范围：[2,6)随机整数