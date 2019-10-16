# -*- coding: utf-8 -*-
'''
Eclair
======

Eclair: CUDA-based Library for Astronomical Image Reduction

This module provides some useful classes and functions
in astronomical image reduction, 
and their processing speed is acceralated by using GPU via CUDA.

This module requires
    1. NVIDIA GPU
    2. CUDA
    3. NumPy, Astropy and CuPy
'''

from param import __version__

from kernel import reduction_kernel as _red

from fitscontainer import FitsContainer

from align import ImAlign, imalign

from combine import imcombine

from fix import fixpix

def reduction(image,bias,dark,flat):
    '''
    This function is equal to the equation:
    result = (image - bias - dark) / flat, but needs less memory.
    Therefore, each inputs must be broadcastable shape.

    Parameters
    ----------
    image : cupy.ndarray
    bias  : cupy.ndarray
    dark  : cupy.ndarray
    flat  : cupy.ndarray
    
    Returns
    -------
    result : cupy.ndarray
    '''

    return _red(image,bias,dark,flat)