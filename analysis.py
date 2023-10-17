def normalize(data: list[float]) -> list[float]:
    """
    Normalized given data so that everything is within the range 0 to 1.
    
    Parameters
    ----------
    data : list[float]
        List of non-normalized measured data.

    Returns
    -------
    new_data : list[float]
        Normalized data values.

    """
    min_data = min(data)
    max_data = max(data)
    max_min_diff = max_data-min_data
    new_data = [(x-min_data)/(max_min_diff) for x in data]

    return new_data


def chi_sq(measured_data:list[float], expected_data:list[float], 
           uncertainty:list[float]):
    """
    Parameters
    ----------
    measured_data : list[float]
        List of measured data.
    expected_data : list[float]
        List of expected data.
    uncertainty : list[float]
        List of uncertainties.

    Returns
    -------
    chi_sq : float
        Chi Squared value.

    """
    chi_sq = 0
    # Converting summation in equation into a for loop
    for i in range(0, len(measured_data)):
        chi_sq += ((measured_data[i] - expected_data[i])/uncertainty[i])**2
    
    chi_sq = (1/(len(measured_data) - 2))*chi_sq

    return chi_sq


def chi_sq_red(measured_data:list[float], expected_data:list[float], 
           uncertainty:list[float], v: int):
    """
    Parameters
    ----------
    measured_data : list[float]
        List of measured data.
    expected_data : list[float]
        List of expected data.
    uncertainty : list[float]
        List of uncertainties.

    Returns
    -------
    chi_sq : float
        Chi Squared value.

    """
    chi_sq = 0
    # Converting summation in equation into a for loop
    for i in range(0, len(measured_data)):
        chi_sq += ((measured_data[i] - expected_data[i])/uncertainty[i])**2
    
    chi_sq = (1/v)*chi_sq

    return chi_sq
