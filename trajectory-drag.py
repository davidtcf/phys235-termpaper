import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # gravitational acceleration (m/s^2)
rho = 1.225  # density of air (kg/m^3)
A = 0.00143  # cross-sectional area of golf ball (m^2)
m = 0.04593  # mass of golf ball (kg)
drag_coefficient = 7 / 2  # drag coefficient

# Initial conditions
v0 = 70  # initial velocity (m/s)
theta = np.radians(9)  # launch angle (radians)
vx0 = v0 * np.cos(theta)  # initial horizontal velocity (m/s)
vy0 = v0 * np.sin(theta)  # initial vertical velocity (m/s)
x0, y0 = 0, 0  # initial position (m)
dt = 0.01  # time step (s)

# Euler's method for projectile motion
def projectile_motion_with_drag(vx, vy, x, y, dt, include_drag=True):
    x_vals, y_vals = [x], [y]
    while y >=0:
        v = np.sqrt(vx**2 + vy**2)
        if include_drag:
            drag_force = -drag_coefficient * rho * A / m
        else:
            drag_force = 0
        ax = drag_force * vx
        ay = drag_force * vy - g
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        x_vals.append(x)
        y_vals.append(y)
    return np.array(x_vals), np.array(y_vals)

# Compute trajectories
x_no_drag, y_no_drag = projectile_motion_with_drag(vx0, vy0, x0, y0, dt, include_drag=False)
x_with_drag, y_with_drag = projectile_motion_with_drag(vx0, vy0, x0, y0, dt, include_drag=True)

# Plot the results
plt.figure(figsize=(10, 6),dpi=150)
plt.plot(x_no_drag, y_no_drag, label="Without Drag", linestyle="--", color="blue")
plt.plot(x_with_drag, y_with_drag, label="With Drag", color="green")
plt.title("Projectile Motion of a Golf Ball with and without Drag Force")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.legend()
plt.grid()

plt.savefig("trajectory-drag.png")
plt.show()
