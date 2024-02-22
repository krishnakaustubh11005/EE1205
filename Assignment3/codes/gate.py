import numpy as np
import matplotlib.pyplot as plt

# Define the time range
t = np.linspace(0, 0.05, 1000)  # 0 to 50 milliseconds

# Define the function
y = 12.5 * np.sin(1000* t)

# Plot the function
plt.plot(t, y, label='V_ab vs t')
plt.xlabel('Time (s)')
plt.ylabel('V_ab(V)')
plt.title('Graph of V_ab vs t')

# Highlight the value at t=5ms using a stem plot
t_highlight = 0.005
index_t_highlight = np.argmin(np.abs(t - t_highlight))
plt.stem(t[index_t_highlight], y[index_t_highlight], linefmt='r', markerfmt='ro', basefmt=' ')

plt.grid(True)
plt.legend()
plt.show()

