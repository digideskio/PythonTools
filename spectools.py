'''
Some random tools for spectral estimation
DMM 05/2013
'''

#Libaries I need
from spectrum import pmtm as pspec
import numpy as np


def nextpow2(i):
    '''
    Find 2^n that is equal to or greater than.
    '''
    n = 2
    while n < i: n = n * 2
    return n
    
    
def pmtm(t,y,K):
    '''
    Multi taper estiamtion of PSD with prolate-spheroidal tapers
    
    IN:
    t - time vector
    y - time series
    K - time-bandwidth product
    
    OUT:
    f - vector of frequencies
    Sh - One sided PSD
    '''
    dt=t[1]-t[0]
    N=y.shape[0]
    Nfft=nextpow2(N)
    z=np.zeros(Nfft-N)
    yz=np.r_[z,y]
    S=pspec(yz,NW=K,show=False)
    #Only keep one sided spectrum
    Sh=S[0:Nfft/2]
    f=np.linspace(0,1/(2*dt),Nfft/2)  #Defines frequency
    return f,Sh
