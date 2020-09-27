"""
solve free-fall in 1D using the Euler Cauchy algorithm 

a(x,v,t) = g
x0,v0 
solve from t = 0, t = 5

"""

import numpy as np
import matplotlib.pyplot as plt

# initial conditions
x0 = 0.0
v0 = 0.0

# parameters
g = -9.8

# initial time
t0 = 0
# final time
tmax = 5
# number of time-points
N = 50

# time-step
dt = (tmax - t0)/N

# array of discrete points
t = np.linspace(t0,tmax,N)
# array for positions
x = np.zeros_like(t)
# array for velocities
v = np.zeros_like(t)

## zeros_like creates an array like the given array and fills
## it with zeros

x[0] = x0
v[0] = v0

"""
x[1] = x[0] + v[0]*dt
v[1] = v[0] + g*dt

x[2] = x[1] + v[1]*dt
v[2] = v[1] + g*dt

"""
## trying to loop through till N for x and v array

for n in range(1,N):
    x[n] = x[n-1] + v[n-1]*dt
    v[n] = v[n-1] + g*dt


# exact solutions
xexact = x0 + v0*t + 0.5*g*t**2
vexact = v0 + g*t


fig, (ax1,ax2) = plt.subplots(2, sharex= True)
ax1.set_ylabel('x')
ax2.set_xlabel('t')
ax2.set_ylabel('v')

ax1.plot(t, x, 'ro', mfc = 'none', ms=5, label='x: numerics')
ax2.plot(t, v,'bs', mfc = 'none', ms=5 , label='x: numerics')

ax1.plot(t, xexact, 'r', label='x: exact')
ax2.plot(t, vexact,'b', label='x: exact')

ax1.legend(loc = 'best')
ax2.legend(loc = 'best')
plt.show()