import matplotlib.pyplot as plt
import numpy as np

# 生成示例数据
np.random.seed(0)  # 设置随机种子，保证结果可重复
x = np.random.rand(50)  # 生成 50 个 0 到 1 之间的随机数
y = np.random.rand(50)
colors = np.random.rand(50)  # 每个点的颜色
area = (30 * np.random.rand(50))**2  # 每个点的面积，放大平方以增大差异

# 绘制散点图
plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=area, c=colors, alpha=0.5)

# 设置图形标题和坐标轴标签
plt.title('Random Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 显示图形
plt.show()
