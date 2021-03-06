# Autogenerated with SMOP 
# CartToSph.m
import math
import numpy
from ZeroTwoPi import ZeroTwoPi

def CartToSph(cn=None,ce=None,cd=None,*args,**kwargs):
    # varargin = CartToSph.varargin
    # nargin = CartToSph.nargin

    #CartToSph converts from cartesian to spherical coordinates
    
    #   [trd,plg] = CartToSph(cn,ce,cd) returns the trend (trd)
#   and plunge (plg) of a line for input north (cn), east (ce), 
#   and down (cd) direction cosines
    
    #   NOTE: Trend and plunge are returned in radians
    
    #   CartToSph uses function ZeroTwoPi
    
    #MATLAB script written by Nestor Cardozo for the book Structural 
#Geology Algorithms by Allmendinger, Cardozo, & Fisher, 2011. If you use
#this script, please cite this as "Cardozo in Allmendinger et al. (2011)"
    
    #Plunge (see Table 2.1)
    plg=math.asin(cd)
# CartToSph.m:17
    #Trend
#If north direction cosine is zero, trend is east or west
#Choose which one by the sign of the east direction cosine
    if cn == 0.0:
        if ce < 0.0:
            trd=numpy.dot(3.0 / 2.0,pi)
# CartToSph.m:24
        else:
            trd=math.pi / 2.0
# CartToSph.m:26
        #Else use Table 2.1
    else:
        trd=math.atan(ce / cn)
# CartToSph.m:30
        if cn < 0.0:
            #Add pi
            trd=trd + math.pi
# CartToSph.m:33
        #Make sure trd is between 0 and 2*pi
        trd=ZeroTwoPi(trd)
# CartToSph.m:36
    
    return trd,plg
    
if __name__ == '__main__':
    pass
    