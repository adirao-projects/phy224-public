import numpy as np


def digits(n: float) -> int:
    """
    Returns the number of digits in a number.

    Parameters
    ----------
    n : float
        Number to be evaluated.

    Returns
    -------
    int
        Number of digits in the number.

    Examples
    --------
    >>> digits(5.1515325326523632)
    17    
    """
    if n==0:
        return 1
    else:
        return abs(np.log10(n))+1

def round(n:float, sigfigs:int) -> float:
    """
    Rounds a number to a specified number of decimal places. using the number
    of digits (as opposed to python rounding system).

    Parameters
    ----------
    n : float
        Number to be rounded.
    sigfigs : int
        Number of significant figures to round to.

    Returns
    -------
    n_rounded: float
        Rounded number.
    """
    return NotImplementedError

def log_uncertainty_converter(real_values: list[float], 
                              uncertainties: list[float]) -> list[float]:
    """
    Converts uncertainty to logarthmic scale.

    Parameters
    ----------
    real_values : list[float]
        Measured current in circuit.
    uncertainties : list[float]
        List of uncertainty values.

    Returns
    -------
    list[float]
        Resulting uncertainty in measured current values.

    """
    
    return (np.log(real_values + uncertainties) - 
            np.log(real_values - uncertainties))/2

def avg_val(x: list[float]) -> float:
    """
    Returns the average value of a list of numbers.

    Parameters
    ----------
    x : list[float]
        List of numbers.

    Returns
    -------
    float
        Average value of the list of numbers.
    """
    return (1/len(x))*sum(x)

def std_dev(x):
    """
    Returns the standard deviation of a list of numbers.
    
    Parameters
    ----------
    x : list[float]
        List of numbers.

    Returns
    -------
    s : float
        Standard deviation of the list of numbers.
    """
    s = 0 
    xbar = avg_val(x)
    for i in range(0, len(x)):
        s += (x[i] - xbar)**2
        
    s = (s/len(x))**(1/2)
    
    return s

def std_err(x: list[float]) -> float:
    """
    Returns the standard error of a list of numbers.
    
    Parameters
    ----------
    x : list[float]
        List of numbers.
    
    Returns
    -------
    float
        Standard error of the list of numbers.
    """
    s = std_dev(x)
    return s/((len(x))**(1/2))


if __name__ == '__main__':
    d = 5.15153253265236328
    print(digits(d))