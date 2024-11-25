# Re-importing necessary libraries and resetting constants after environment reset
import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # gravitational acceleration (m/s^2)
rho = 1.225  # density of air at sea level (kg/m^3)
A = 0.00143  # cross-sectional area of golf ball (m^2)
m = 0.04593  # mass of golf ball (kg)
drag_coefficient = 7 / 2  # drag coefficient
T0 = 288.15  # sea level temperature (K)
a = 6.5e-3  # temperature lapse rate (K/m)
alpha = 2.5  # exponent for air
S0_omega_m = 0.25  # Magnus force coefficient (S0 * omega / m)

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

# Euler's method including both drag and Magnus forces
def projectile_motion_with_drag_and_magnus(vx, vy, x, y, dt, include_drag=True):
    x_vals, y_vals = [x], [y]
    while y >= 0:
        # Height-dependent air density

        rho_y = rho * (1 - (a * y) / T0)**alpha if include_drag else 0
        # Drag and Magnus force components
        drag_fx = -drag_coefficient * rho_y * A * vx
        drag_fy = -drag_coefficient * rho_y * A * vy
        magnus_fx = -S0_omega_m * vy
        magnus_fy = S0_omega_m * vx
        
        # Accelerations
        ax = drag_fx / m + magnus_fx
        ay = drag_fy / m + magnus_fy - g
        
        # Update velocities
        vx += ax * dt
        vy += ay * dt
        
        # Update positions
        x += vx * dt
        y += vy * dt
        
        x_vals.append(x)
        y_vals.append(y)
    return np.array(x_vals), np.array(y_vals)

# Compute trajectory with drag and Magnus force
x_drag_magnus, y_drag_magnus = projectile_motion_with_drag_and_magnus(vx0, vy0, x0, y0, dt, include_drag=False)


# Plot the results
plt.figure(figsize=(10, 6), dpi=150)
plt.plot(x_drag_magnus, y_drag_magnus, label="With Magnus Force only",color="red")
plt.plot(x_no_drag, y_no_drag, label="Idealistic Trajectory", linestyle="--", color="blue")
plt.title("Projectile Motion of a Golf Ball: How Magnus Force Affects Trajectory")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.legend()
plt.grid()
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.tight_layout()
plt.savefig("trajectory-magnus.png")
plt.show()
