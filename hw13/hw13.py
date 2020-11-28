import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12, 13, 0.1)
y1 = x + 0.25
y2 = x
y3 = x - 0.25

plt.xlabel("Alice's Availability")
plt.ylabel("Bob's Availability")
plt.title("Distribution of Meeting Times")
# plt.axvspan(12, 13, alpha=0.5, color='b')
# plt.axhspan(12, 13, alpha=0.5, color='r')
plt.plot(
    x, y1,
    x, y2,
    x, y3
)
plt.fill_between(x, y1, y3, color="grey", alpha=0.5)
plt.show()
