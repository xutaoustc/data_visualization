import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
ymin = [1, 3, 2, 4, 1]
ymax = [2, 4, 3, 5, 2]

# 创建图形
plt.figure(figsize=(8, 6))

# 绘制垂直线
plt.vlines(x, ymin, ymax, colors='r', linestyles='--', label='Vertical Lines')

# 添加标签和标题
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Example of vlines in Matplotlib')
plt.legend()

# 显示图形
plt.grid(True)
plt.show()
