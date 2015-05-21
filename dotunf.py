import numpy as np
import sys
import os
import fortranfile

def runf(fname,shape=None,prec=np.double):
    '''runf(fname,shape=None,prec=np.double)'''
    fd = open(fname, 'rb')
    if shape is None:
        data = np.fromfile(file=fd, dtype=prec)
    else:
        data = np.fromfile(file=fd, dtype=prec).reshape(shape)
    fd.close()
    return data


def wunf(arr,outfilename,prec='d'):
    '''wunf(arr,inputfilename,prec='d')'''
    f = fortranfile.FortranFile(outfilename)
    f.writeReals(arr, prec=prec)


def read_unf(inputfilename,prec='d'):
    '''wunf(arr,inputfilename,prec='d')'''
    f = fortranfile.FortranFile(inputfilename)
    return f.readReals(prec=prec)
    
