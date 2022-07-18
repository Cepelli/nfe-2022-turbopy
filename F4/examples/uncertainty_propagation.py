import numpy as np

def addition_uncertainty(x_tuple, y_tuple, addition=True):
    """computes the uncertainty error for addition/subtraction of two values with uncertainty
    where z = x+-y

    Parameters
    ----------
    x_tuple : tuple of float, int, np.ndarray
        measured values and uncertainty
    y_tuple : tuple of float, int, np.ndarray
        measursed values and uncertainty
    addition : bool
        if true, it adds x and y. If false, it subtracts

    Returns
    -------
    z, delta_z : tuple
        the addition of x and y with the uncertainty
    """
    x_measured = x_tuple[0]
    x_uncertainty = x_tuple[1]

    y_measured = y_tuple[0]
    y_uncertainty = y_tuple[1]

    if addition is False:
        z = x_measured - y_measured
    else:
        z = x_measured + y_measured
    delta_z = np.sqrt(x_uncertainty**2 + y_uncertainty**2)

    return (z, delta_z)


def constant_uncertainty(x_tuple, constant):
    """computes the uncertainty error for constant times values with uncertainty
    where z = cx

    Parameters
    ----------
    x_tuple : tuple of float, int, np.ndarray
        measured values and uncertainty
    constant : float, int
        the value of the constant that x is multiplied by 
    """
    x_measured = x_tuple[0]
    x_uncertainty = x_tuple[1]

    z = constant*x_measured
    delta_z = np.absolute(constant) * x_uncertainty
    return (z, delta_z)


def division_uncertainty(x_tuple, y_tuple):
    """computes the uncertainty error for division of two values with uncertainty
    where z = x/y

    Parameters
    ----------
    x_tuple : tuple of float, int, np.ndarray
        measured values and uncertainty
    y_tuple : tuple of float, int, np.ndarray
        measursed values and uncertainty
    """
    x_measured = x_tuple[0]
    x_uncertainty = x_tuple[1]

    y_measured = y_tuple[0]
    y_uncertainty = y_tuple[1]

    z = x_measured/y_measured
    delta_z = np.absolute(x_measured/y_measured)*np.sqrt((x_uncertainty/x_measured)**2 + (y_uncertainty/y_measured)**2)
    return (z, delta_z)

def multiplication_uncertainty(x_tuple, y_tuple):
    """computes the uncertainty error for multiplication of two values with uncertainty
    where z = x*y

    Parameters
    ----------
    x_tuple : tuple of float, int, np.ndarray
        measured values and uncertainty
    y_tuple : tuple of float, int, np.ndarray
        measursed values and uncertainty
    """
    x_measured = x_tuple[0]
    x_uncertainty = x_tuple[1]

    y_measured = y_tuple[0]
    y_uncertainty = y_tuple[1]

    z = x_measured * y_measured
    delta_z = np.absolute(x_measured*y_measured)*np.sqrt((x_uncertainty/x_measured)**2 + (y_uncertainty/y_measured)**2)
    return (z, delta_z)


def power_uncertainty(x_tuple, npower):
    """computes the uncertainty error for power of values with uncertainty
    where z = x^n

    Parameters
    ----------
    x_tuple : tuple of float, int, np.ndarray
        measured values and uncertainty
    npower : float, int
        the value of the power that x is raised to 
    """
    x_measured = x_tuple[0]
    x_uncertainty = x_tuple[1]

    z = x_measured**npower
    delta_z = np.absolute(npower) * x_measured**(npower-1) * x_uncertainty
    return (z, delta_z)


def log_uncertainty(x_tuple):
    """computes the uncertainty error for when x is the argument of a logarithm with uncertainty
    where z = ln(x)

    Parameters
    ----------
    x_tuple : tuple of float, int, np.ndarray
        measured values and uncertainty 
    """
    x_measured = x_tuple[0]
    x_uncertainty = x_tuple[1]

    z = np.log(x_measured)
    delta_z = x_uncertainty/x_measured
    return (z, delta_z)