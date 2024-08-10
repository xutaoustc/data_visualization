import matplotlib.pyplot as plt
import numpy as np

# 生成网格数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# 定义一个函数 Z = f(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 绘制等高线图
plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, Z, levels=10, colors='black')
plt.contourf(X, Y, Z, levels=10, cmap='viridis')  # 填充等高线

# 添加颜色条
plt.colorbar()

# 添加等高线标签
plt.clabel(contour, inline=True, fontsize=8)

# 添加标题和标签
plt.title('Contour Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 显示图形
plt.show()
