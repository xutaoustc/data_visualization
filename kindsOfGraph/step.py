import matplotlib.pyplot as plt
import numpy as np

# 生成示例数据
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# 绘制阶梯图
plt.figure(figsize=(10, 6))
plt.step(x, y, where='mid', color='blue', label='Sine wave (mid)')
plt.step(x, y + 1, where='pre', color='green', linestyle='--', label='Sine wave + 1 (pre)')
plt.step(x, y - 1, where='post', color='red', linestyle=':', label='Sine wave - 1 (post)')

# 添加标题和标签
plt.title('Step Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# 显示图形
plt.show()
