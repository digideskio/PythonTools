'''
DMM 05/2013
Random tools for time series handling
'''

import numpy as np

def tcrop(t,y,t1,t2):
    '''
    Crop a time series to a given interval
    IN:
    t - time vector
    y - time series
    t1,t2 - crop interval
    OUT
    tc - cropped time vector
    yc - cropped time series
    '''
    i=np.nonzero(np.logical_and(t>=t1,t<=t2))
    tc=t[i]
    yc=y[i]
    return tc,yc