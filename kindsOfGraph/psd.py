import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# 生成一个随机信号
np.random.seed(0)
fs = 500  # 采样频率
t = np.arange(0, 10, 1/fs)  # 时间轴
signal = np.sin(2*np.pi*50*t) + np.random.randn(len(t))  # 50Hz 正弦信号和噪声

# 计算功率谱密度
frequencies, psd = welch(signal, fs, nperseg=1024)

# 绘制功率谱密度图
plt.figure(figsize=(10, 6))
plt.semilogy(frequencies, psd)
plt.title('Power Spectral Density')
plt.xlabel('Frequency (Hz)')
plt.ylabel('PSD (dB/Hz)')
plt.grid(True)
plt.show()