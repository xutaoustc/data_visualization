import matplotlib.pyplot as plt
import numpy as np

# 生成正态分布数据
np.random.seed(0)
data = np.random.randn(1000)  # 生成1000个标准正态分布的随机数

# 绘制直方图
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='blue', alpha=0.7, edgecolor='black')

# 添加标题和标签
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 显示图形
plt.show()
