import numpy as np
import matplotlib.pyplot as plt

# 生成两个示例信号
fs = 500  # 采样频率
t = np.arange(0, 10, 1/fs)  # 时间向量

# 信号1：基本为 5Hz 的正弦波
signal1 = np.sin(2 * np.pi * 5 * t)

# 信号2：5Hz 的正弦波，加上10Hz的噪声
signal2 = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t)

# 计算并绘制信号的相干性
plt.figure(figsize=(10, 6))
Cxy, f = plt.cohere(signal1, signal2, NFFT=256, Fs=fs, noverlap=128)

plt.title('Coherence between Signal 1 and Signal 2')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Coherence')
plt.grid(True)
plt.show()
