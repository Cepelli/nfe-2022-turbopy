# %% [markdown]
"""
This example problem of a mass-spring-damper system is taken 
from [a blog post by Hans-Petter 
Halvorsen](https://www.halvorsen.blog/documents/programming/python/resources/powerpoints/Mass-Spring-Damper%20System%20with%20Python.pdf)
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import pandas as pd


# %% [markdown]
"""
The goal is to solve for the position, $x_1(t)$,
and velocity, $x_2(t)$, of the mass as a function of time. 

We will store the values in an array of shape (`len(t)`, 2):
$[ [x_1(t_0), x_2(t_0)], [x_1(t_1), x_2(t_1)], ... ]$,
where `t` is an array of timesteps.

We are using the solver [scipy.integrate.solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp).
"""

# %% [markdown]
"""
So first we need to define a function that returns the
derivatives of $x_1$ and $x_2$ in an array.

$\frac{dx_1}{dt} = x_2$  
$\frac{dx_2}{dt} = \frac{1}{m}(F - kx_1 - cx_2)$
"""
def mydiff(t, x): 
    """Compute derivative of position and velocity
    for mass-spring-damper system.

    Parameters
    ----------
    x : list of float
        position and velocity of mass
    t : float
        timestep

    Returns
    -------
    dxdt : list of float
        derivatives of position and velocity of the mas
    """
    c = 4 # Damping constant
    k = 2 # Stiffness of the spring
    m = 20 # Mass
    F = 5 # External force
    dx1dt = x[1] 
    dx2dt = (F - c*x[1] - k*x[0])/m
    dxdt = [dx1dt, dx2dt]
    return dxdt

# %% [markdown]
"""
For example...
"""
mydiff(x=[0, 0], t=0)

# %% [markdown]
"""
Set the initial conditions, `x_init`, 
$[x_1(t=0)=0, x_2(t=0)=0]$:
"""
x_init = [0, 0]

# %% [markdown]
"""
Initialize the start time (`tstart`), 
stop time (`tstop`), and time increment (`tincrement`),
and create the array of timesteps.
"""
tstart = 0
tstop = 61
tincrement = 0.1
t = np.arange(tstart, tstop, tincrement)

# %% [markdown]
"""
Now, we can solve system of two first-order
ordinary differential equations (ODEs) at each
timestep in `t` in one more line of Python:
"""
sol = solve_ivp(mydiff, 
                (tstart, tstop), 
                x_init,
                t_eval=t)

# %% [markdown]
# Plot the results
x1 = sol.y[0,:]
x2 = sol.y[1,:]
plt.plot(sol.t,x1)
plt.plot(sol.t,x2)
plt.title('Simulation of Mass-Spring-Damper System')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend(["x1 (position)", "x2 (velocity)"])
plt.grid()
plt.show()

# %% [markdown]
"""
But that's not very exciting...we only ran
a simulation for one particular set of 
initial conditions and spring-mass-damper
system properties.

And this is a seminar about working with data, so we
need more of it!

Let's generalize our function for computing derivatives.

"""
def mydiff2(t, x, c, k, m, F): 
    """Compute derivative of position and velocity
    for mass-spring-damper system.

    Parameters
    ----------
    x : list of float
        position and velocity of mass
    t : float
        timestep
    c : float
        damping constant
    k : float
        spring constant
    m : float
        mass
    F : float
        force applied to mass in x-direction

    Returns
    -------
    dxdt : list of float
        derivatives of position and velocity of the mass
    """
    dx1dt = x[1] 
    dx2dt = (F - c*x[1] - k*x[0])/m
    dxdt = [dx1dt, dx2dt]
    return dxdt

# %% [markdown]
"""
We're interested in exploring solutions for a range of
input parameters and initial conditions.

Let's keep our mass constant:
"""
m = 20
"""
But I'd like to vary `c`, `k`, and `F`:
"""
c_array = np.linspace(2, 4, 11)
k_array = np.linspace(1, 3, 11)
F_array = np.linspace(3, 5, 11)

# %% [markdown]
msd = pd.DataFrame(columns=('c', 'k', 'F', 'x1', 'x2'))
for c in c_array:
    for k in k_array:
        for F in F_array:
            sol = solve_ivp(mydiff2, (tstart, tstop), x_init, t_eval=t, 
                          args=(c, k, m, F)) 
            values_to_add = {'c': c, 'k': k, 'F': F,
                             'x1': sol.y[0,:], 'x2': sol.y[1,:]}
            row_to_add = pd.Series(values_to_add)
            msd = msd.append(row_to_add, ignore_index=True)

# %%
msd.shape
# %%
msd.columns
# %%
type(msd['c'][0])
# %%
type(msd['x1'][0])

# %% [markdown]
# Plot one of the rows
rownum = 0
plt.plot(t,msd['x1'][rownum])
plt.plot(t,msd['x2'][rownum])
plt.title(f"Mass-Spring-Damper (c={msd['c'][rownum]}, "
                              f"k={msd['k'][rownum]}, "
                              f"F={msd['F'][rownum]})")
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend(["x1 (position)", "x2 (velocity)"])
plt.grid()
plt.show()
# %%

# %% [markdown]
"""
We might want to do that again, so let's create a 
plotting function.
"""
def plot_msd_rownum(msd, rownum):
    plt.plot(t,msd['x1'][rownum])
    plt.plot(t,msd['x2'][rownum])
    plt.title(f"Mass-Spring-Damper (c={msd['c'][rownum]}, "
                                  f"k={msd['k'][rownum]}, "
                                  f"F={msd['F'][rownum]})")
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.legend(["x1 (position)", "x2 (velocity)"])
    plt.grid()
    plt.show()

# %%
plot_msd_rownum(msd, 100)
# %%
"""
What if we want to plot many rows?
"""
def plot_list_of_msd_rows(msd, list_of_rows):
    for rownum in list_of_rows:
        plt.plot(t,msd['x1'][rownum])
        plt.plot(t,msd['x2'][rownum])
        plt.title(f"Mass-Spring-Damper (c={msd['c'][rownum]}, "
                                      f"k={msd['k'][rownum]}, "
                                      f"F={msd['F'][rownum]})")
        plt.xlabel('t')
        plt.ylabel('x(t)')
        plt.legend(["x1 (position)", "x2 (velocity)"])
        plt.grid()
        plt.show()

# %%
plot_list_of_msd_rows(msd, [i for i in range(0, 1000, 100)])

# %%
"""
Well, actually, we want to put them all on the same plot.
"""
def plot_list_of_msd_rows_one_plot(msd, list_of_rows):
    for rownum in list_of_rows:
        plt.plot(t, msd['x1'][rownum], 'b--')
        plt.plot(t, msd['x2'][rownum], 'r-')
    plt.title(f"Mass-Spring-Damper") 
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.legend(["x1 (position)", "x2 (velocity)"])
    plt.grid()
    plt.show()
# %%
plot_list_of_msd_rows_one_plot(msd, [i for i in range(0, 1000, 100)])

# %%
"""
Let's add columns for the peak position and velocity.
"""
msd['x1_max'] = msd.apply(lambda row: np.max(row.x1), axis=1)
msd['x2_max'] = msd.apply(lambda row: np.max(row.x2), axis=1)

# %%
msd['x1_max'][0:10]

# %% [markdown]
"""
And plot it.

First, the max positions:
"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
img = ax.scatter(msd['c'], msd['k'], msd['F'], c=msd['x1_max'], 
                 cmap=plt.hot())

ax.set_xlabel('c')
ax.set_ylabel('k')
ax.set_zlabel('F')

cax = fig.add_axes([0.25, 0.9, 0.5, 0.03])
fig.colorbar(img, orientation='horizontal', cax=cax)

plt.title('Maximum Position')
plt.show()

# %% [markdown]
"""
Then, the max velocities:
"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
img = ax.scatter(msd['c'], msd['k'], msd['F'], c=msd['x2_max'], 
                 cmap=plt.hot())

ax.set_xlabel('c')
ax.set_ylabel('k')
ax.set_zlabel('F')

cax = fig.add_axes([0.25, 0.9, 0.5, 0.03])
fig.colorbar(img, orientation='horizontal', cax=cax)

plt.title('Maximum Velocity')
plt.show()


# %%
