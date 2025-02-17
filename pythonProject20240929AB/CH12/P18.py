import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0.0, 20.0, 1)
s = np.linspace(0, 10, 20)
plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.subplot(2, 1, 2)
plt.plot(t, s, 'r-')
plt.show( )
