import os
import math
import textwrap

def block_print(data: list[str], title: str, delimiter='=') -> None:
    """
    Prints a formated block of text with a title and delimiter

    Parameters
    ----------
    data : list[str]
        Text to be printed (should be input as one block of text).
    title : str
        Title of the data being output.
    delimiter : str, optional
        Delimiter to be used. The default is '='.

    Returns
    -------
    None.

    Examples
    --------
    >>> r_log = 100114.24998718781
    >>> r_dec = 0.007422298127465114
    >>> data = [f'r^2 value (log): {r_log}', 
                f'r^2 value (real): {r_dec}']
    >>> block_print(data, 'Regression Coefficient', '=')
    ============================ Regression Coefficient ============================
    r^2 value (log): 100114.24998718781
    r^2 value (real): 0.007422298127465114
    ================================================================================
    """
    term_size = os.get_terminal_size().columns
    
    breaks = 1
    str_len = len(title)+2
    while  str_len >= term_size:
        breaks += 1
        str_len = math.ceil(str_len/2)
        
    
    str_chunk_len = math.ceil(len(title)/breaks)
    str_chunks = textwrap.wrap(title, str_chunk_len)
    output = ''
    for chunk in str_chunks:
        border = delimiter*(math.floor((term_size - str_chunk_len)/2)-1)
        output = f'{border} {chunk} {border}\n'
    
    output=output[:-1]
    
    output+= '\n'+ '\n'.join(data) + '\n'
    output+=delimiter*term_size
    
    print(output)


if __name__ == '__main__':
    r_log = 100114.24998718781
    r_dec = 0.007422298127465114
    data = [f'r^2 value (log): {r_log}', f'r^2 value (real): {r_dec}']
    block_print(data, 'Regression Coefficient', '=')