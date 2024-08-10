import matplotlib.pyplot as plt

# 数据
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# 创建图形
plt.figure(figsize=(8, 8))

# 绘制饼图
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# 添加标题
plt.title('Example of Pie Chart in Matplotlib')

# 显示图形
plt.show()
