import matplotlib.pyplot as plt
import numpy as np

a = np.arange(10)

plt.subplot(211)
plt.plot(a, a * 1.5, a, a * 2.5, a, a * 3.5, a, a * 4.5)

# 颜色字符、风格字符、标记字符
plt.subplot(212)
plt.plot(a, a*1.5, "go-", a, a * 2.5, "rx", a, a * 3.5, "*", a, a * 4.5, "b-.")


plt.show()
