import numpy as np


class Func:
    def __init__(self, f, g, x0, x1, y0, y1):
        self.f = f
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        if g == 'rect':
            def g(x, y):
                return (1 if (self.x0 <= x <= self.x1 and self.y0 <= y <= self.y1) else -1)  
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
    return area*f_mean

