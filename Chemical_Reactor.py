import matplotlib.pyplot as plt

# Initial quantities
a = 100  # substance A (grams)
b = 50   # substance B (grams)
c = 0    # substance C (grams)

# Rate constants
k1 = 0.008
k2 = 0.002

# Time parameters
dt = 0.1  # time step
num_steps = 100  # number of simulation steps

# Lists to store time and corresponding quantities of substances A, B, and C
time_points = [0]
a_values = [a]
b_values = [b]
c_values = [c]

# Simulation loop
for step in range(num_steps):
    # Calculate the rate of formation of C
    rate_c = k1 * a * b - k2 * c
    
    # Update quantities based on the rate and time step
    a -= k1 * a * b * dt
    b -= k1 * a * b * dt
    c += rate_c * dt
    
    # Append current time and quantities to the lists
    time_points.append((step + 1) * dt)
    a_values.append(a)
    b_values.append(b)
    c_values.append(c)
    
    # Print quantities at each time step
    print(f"Time: {time_points[-1]:.2f}, A: {a_values[-1]:.2f}, B: {b_values[-1]:.2f}, C: {c_values[-1]:.2f}")

# Plot the results
plt.clf()
plt.plot(time_points, a_values, label='Substance A')
plt.plot(time_points, b_values, label='Substance B')
plt.plot(time_points, c_values, label='Substance C')
plt.title('Quantities of Substances A, B, and C over Time')
plt.xlabel('Time (units)')
plt.ylabel('Quantity (grams)')
plt.legend()
plt.grid(True)
plt.show()
plt.pause(0.001)
