import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# 创建日期数据
dates = pd.date_range('2024-01-01', periods=10)
values = [10, 15, 7, 10, 5, 12, 18, 14, 16, 9]

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制日期数据
plt.plot_date(dates, values, linestyle='-', marker='o', color='b')

# 格式化日期显示
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# 添加标签和标题
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Example of Plot Date in Matplotlib')

# 自动旋转日期标签
plt.gcf().autofmt_xdate()

# 显示图形
plt.grid(True)
plt.show()
