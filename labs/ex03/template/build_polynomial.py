# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    augmented=np.ones((x.shape[0],1))
    x=x.reshape((x.shape[0],1))
    for d in range(1,degree+1):
        augmented=np.concatenate([augmented,x**d],1)
    
    return augmented
