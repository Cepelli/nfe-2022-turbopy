from monte_carlo_b import *

def test_MonteCarlo_double_rectangle_area():
    """Check the area of a rectangle."""

    def f(x, y):
        return 1

    func_rect = Func(f=f, g='rect', x0=0, x1=2, y0=3, y1=4.5)

    np.random.seed(8)      # must fix the seed!
    I_expected = 3.121092  # computed with this seed

    I_computed = MonteCarlo_double(func_rect, dx0=0, dx1=3, dy0=2, dy1=5, n=1000)

    assert abs(I_expected - I_computed) < 1E-14

def test_MonteCarlo_double_circle_r():
    """Check the integral of r over a circle with radius 2."""
    def g(x, y):
        xc, yc = 0, 0  # center
        R = 2          # radius
        return  R**2 - ((x-xc)**2 + (y-yc)**2)

    x0 = -2;  x1 = 2;  y0 = -2;  y1 = 2
    n = 1000
    np.random.seed(6)
    I_expected = 16.7970837117376384  # Computed with this seed
    I_computed = MonteCarlo_double(
        lambda x, y: np.sqrt(x**2 + y**2),
        g, x0, x1, y0, y1, n)
    assert abs(I_expected - I_computed) < 1E-15
