import numpy as np


class Func:
    def __init__(self, f, **gargs):
        self.f = f
        if gargs['gtype'] == 'rect':
            def g(x, y):
                return (1 if (gargs['x0'] <= x <= gargs['x1'] and gargs['y0'] <= y <= gargs['y1']) else -1)  
            self.g = g
        elif gargs['gtype'] == 'circ':
            def g(x, y):
                return  gargs['R']**2 - ((x-gargs['xc'])**2 + (y-gargs['yc'])**2)
            self.g = g


def MonteCarlo_double(f, dx0, dx1, dy0, dy1, n):
    """
    Monte Carlo integration of f over a domain g>=0, embedded
    in a rectangle [x0,x1]x[y0,y1]. n^2 is the number of
    random points.
    """
    # Draw n**2 random points in the rectangle
    x = np.random.uniform(dx0, dx1, n)
    y = np.random.uniform(dy0, dy1, n)
    # Compute sum of f values inside the integration domain
    f_sum = 0
    num_inside = 0   # number of x,y points inside domain (g>=0)
    for i in range(len(x)):
        for j in range(len(y)):
            if f.g(x[i], y[j]) >= 0:
                num_inside = num_inside + 1
                f_sum = f_sum + f.f(x[i], y[j])
    f_mean = f_sum/num_inside
    area = num_inside/(n**2)*(dx1 - dx0)*(dy1 - dy0)
    I_computed = area * f_mean
    return I_computed

