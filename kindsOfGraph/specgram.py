import numpy as np
import matplotlib.pyplot as plt

# 生成一个包含多个频率成分的信号
fs = 1000  # 采样频率
t = np.arange(0, 10, 1/fs)  # 时间向量

# 生成一个频率随时间变化的信号
signal = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 100 * t * (1 + 0.01 * t)) + np.random.randn(len(t)) * 0.1

# 使用 specgram 绘制功率谱图
plt.figure(figsize=(10, 6))
plt.specgram(signal, NFFT=256, Fs=fs, noverlap=128, cmap='viridis')

plt.title('Spectrogram of the Signal')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.colorbar(label='Intensity (dB)')
plt.show()
