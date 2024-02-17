import numpy as np
import matplotlib.pyplot as plt

# Define function parameters
omega = 1000
time_ms = 5  # Time in milliseconds

# Convert time to seconds
time_s = time_ms / 1000

# Calculate sine value at 5ms
sine_value = 12.5*np.sin(omega * time_s)

# Create time array for plotting
time = np.linspace(0, 0.02, 1000)  # Create 1000 points between 0 and 0.02 seconds

# Calculate sine values for plotting
sine_values = 12.5*np.sin(omega * time)

# Mark the value at 5ms on the plot
plt.plot(time, sine_values)
plt.axvline(time_s, color='red', linestyle='--', label='5ms')  # Vertical line at 5ms

plt.scatter(time_s, sine_value, color='red', marker='o')
# Annotate the sine value at 5ms
plt.annotate(f" {sine_value:.4f}", xy=(time_s, sine_value),
             xytext=(time_s + 0.002, sine_value + 0.05),
             arrowprops=dict(facecolor='red', arrowstyle='->'))
plt.xlabel("Time (s)")
plt.ylabel("Voltage between terminals a and b")
plt.title("V_ab(t) vs t")
plt.grid(True)
plt.legend()
plt.show()

print(f"Sin value at 5ms: {sine_value:.4f}")
