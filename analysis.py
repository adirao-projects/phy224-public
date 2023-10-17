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