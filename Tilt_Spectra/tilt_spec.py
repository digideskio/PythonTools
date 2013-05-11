'''
DMM 05/2013
Compute PSD with multitaper method for tilt data
'''

from spectrum import pmtm
import numpy as np
from matplotlib import pyplot as pl
from matplotlib import rc
import spectools as spec
import timestools as times


#Define list of files to be read
path="/Users/dmelgarm/Research/Data/Tilts/"
files=["misalignment.nw.ne_reverse","misalignment.nw.nw_reverse","misalignment.nw.se_reverse","misalignment.nw.sw_reverse", \
    "misalignment.sw.ne_reverse","misalignment.sw.nw_reverse","misalignment.sw.se_reverse","misalignment.sw.sw_reverse"]
#Iinitalize plotting
pl.close("all") #plots
rc('text', usetex=True) #To use Latex
#read GPS and seismic array data
dgps=np.loadtxt(path+"gps_array.txt")
tgps=dgps[:,0]
ewgps=dgps[:,2]
dacc=np.loadtxt(path+"accel_array.txt")
tacc=dacc[:,0]
ewacc=dacc[:,2]
#Loop through files
for k in range(len(files)):
    print "Working on file %s" %path+files[k]
    #Read in file
    d=np.loadtxt(path+files[k])
    t=d[:,0]
    ew=d[:,2]
    #Re read array data
    tgps=dgps[:,0]
    ewgps=dgps[:,2]
    tacc=dacc[:,0]
    ewacc=dacc[:,2]
    #Match times between array data and kalman filter data
    tgps,ewgps=times.tcrop(tgps,ewgps,t.min(),t.max())
    tgps=tgps-tgps[0]
    tacc,ewacc=times.tcrop(tacc,ewacc,t.min(),t.max())
    tacc=tacc-tacc[0]
    #Cut to interval
    t1=50
    t2=200
    tgps,ewgps=times.tcrop(tgps,ewgps,t1,t2)
    tgps=tgps-tgps[0]
    ewgps=ewgps-ewgps[0]
    tacc,ewacc=times.tcrop(tacc,ewacc,t1,t2)
    tacc=tacc-tacc[0]
    ewacc=ewacc-ewacc[0]
    t=t-t[0]
    t,ew=times.tcrop(t,ew,t1,t2)
    t=t-t[0]
    ew=ew-ew[0]
    #Get spectra
    f,S=spec.pmtm(t,ew,2.5)
    facc,Sacc=spec.pmtm(tacc,ewacc,2.5)
    fgps,Sgps=spec.pmtm(tgps,ewgps,2.5)
    #Plot the thing
    pl.loglog(f,S,facc,Sacc,fgps,Sgps)
    pl.legend(('GPS+accel','Accel array','GPS array'))
    pl.grid(True, which="both") #Make sure it draws log grid
    pl.xlabel(r'Frequency (\textrm{Hz})')
    pl.ylabel(r'PSD (deg^2/\textrm{Hz})')
    pl.savefig(path+files[k]+".spec.png")
    pl.cla()
    #Plot the time series for good measure
    pl.plot(t,ew,tacc,ewacc,tgps,ewgps)
    pl.legend(('GPS+accel','Accel array','GPS array'))
    pl.grid(True, which="both")
    pl.xlabel(r'Time (\textrm{s})')
    pl.ylabel(r'EW Tilt (deg)')
    pl.savefig(path+files[k]+".png")
    pl.cla()
   
   
