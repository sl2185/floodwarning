import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as dts

def polyfit(dates,levels,p):
    
    '''
    Computes a lest-squares fit of a polynomial of degree p to water level data
    Args: 
        Dates: List of datetime objects
        Levels: List of floats
        P(int): Polynomial degree to be fitted
    '''
    #Convert list of datetime objects into a 
    date_float_list = dts.date2num(dates)

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(date_float_list - date_float_list[0],levels,p)

    # Convert coefficient into a polynomial that can be evaluated.
    poly =np.poly1d(p_coeff)
    
    return poly, p_coeff[-1]