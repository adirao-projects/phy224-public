from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def curve_fit_shortcut(model_function: function, x: list, y:list, x_error: list, y_error: list, guess_params: list = []):
    """
    A shortcut to the scipy.optimize.curve_fit function.
    
    Parameters
    ----------
    model_function : function
        The model function to be fitted to the data.
        x : list
        A list of the x data.
        y : list
        A list of the y data.
        x_error : list
        A list of the x error.
        y_error : list
        A list of the y error.
        guess_params : list
        A list of the guess parameters.
        
    Returns
    -------
    popt : list
        A list of the fitted parameters.
    pov : list
        A list of the fitted parameters error.
    pstd: list
        A list of the fitted parameters standard deviation.
    """
    popt, pcov = curve_fit(model_function, x, y, p0 = guess_params, 
                           sigma = y_error, absolute_sigma = True)
    pstd = np.sqrt(np.diag(pcov))
    return popt, pcov, pstd

def residual_calculation(model_function: function, 
                         parameters: tuple, y_data: list) -> list[float]:
    """
    Calculates the residuals of measured data against curve fit model
    
    Parameters
    ----------
    model_function : function
        The model function to fit the data.
    parameters : list
        Curve fit parameters.
    y : list
        Measured y-data for the residuals to be calculated from
    guess_params : list
        A list of the guess parameters.
        
    Returns
    -------
    residuals : list[float]
        Calculated residual values.
    """   
    best_fit_data = model_function(*parameters)
    residuals = []
    for v, u in zip(best_fit_data, y_data):
        residuals.append(v-u)
    
    return residuals

def quick_plot(x_data: list[float], y_data: list[float]) -> None:
    """
    Quick plot of x and y data
    
    Parameters
    ----------
    x_data : list[float]
        x data to be plotted
    y_data : list[float]
        y data to be plotted
        
    Returns
    -------
    None
    """
    plt.figure()
    plt.scatter(x_data, y_data, size=15, color='red', marker='+')
    plt.show()