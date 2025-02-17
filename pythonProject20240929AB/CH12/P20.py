import matplotlib.pyplot as plt
import numpy as np
X = np.linspace(-np.pi,
                np.pi,
                256,
                endpoint=True)
Y = np.cos(X)
plt.figure(figsize=(8,8))

plt.subplot(2,2,1)
plt.plot(X, Y, color="blue")
plt.title('subplot(2,2,1)')

# plt.subplot(2,2,3)
# plt.plot(X, Y*-1, color="red")
# plt.title('subplot(2,2,3)')

# plt.subplot(2,2,(2,4))
# plt.plot(X, Y*-1, color="green")
# plt.plot(X, Y, color="black")
# plt.title('subplot(2,2,(3,4))')
plt.show( )
