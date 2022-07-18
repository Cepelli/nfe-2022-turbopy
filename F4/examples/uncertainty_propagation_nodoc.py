import numpy as np

def addition_uncertainty(x_tuple, y_tuple, addition=True):
    
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
    
    x_measured = x_tuple[0]
    x_uncertainty = x_tuple[1]

    z = constant*x_measured
    delta_z = np.absolute(constant) * x_uncertainty
    return (z, delta_z)


def division_uncertainty(x_tuple, y_tuple):
    
    x_measured = x_tuple[0]
    x_uncertainty = x_tuple[1]

    y_measured = y_tuple[0]
    y_uncertainty = y_tuple[1]

    z = x_measured/y_measured
    delta_z = np.absolute(x_measured/y_measured)*np.sqrt((x_uncertainty/x_measured)**2 + (y_uncertainty/y_measured)**2)
    return (z, delta_z)

def multiplication_uncertainty(x_tuple, y_tuple):
    
    x_measured = x_tuple[0]
    x_uncertainty = x_tuple[1]

    y_measured = y_tuple[0]
    y_uncertainty = y_tuple[1]

    z = x_measured * y_measured
    delta_z = np.absolute(x_measured*y_measured)*np.sqrt((x_uncertainty/x_measured)**2 + (y_uncertainty/y_measured)**2)
    return (z, delta_z)


def power_uncertainty(x_tuple, npower):
    
    x_measured = x_tuple[0]
    x_uncertainty = x_tuple[1]

    z = x_measured**npower
    delta_z = np.absolute(npower) * x_measured**(npower-1) * x_uncertainty
    return (z, delta_z)


def log_uncertainty(x_tuple):
    
    x_measured = x_tuple[0]
    x_uncertainty = x_tuple[1]

    z = np.log(x_measured)
    delta_z = x_uncertainty/x_measured
    return (z, delta_z)