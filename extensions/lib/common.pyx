import numpy as np
cimport numpy as np
cimport cython
from numpy cimport *

cdef extern from "numpy/arrayobject.h":
    void _import_array()

cdef extern from "math.h":
    double log(double x)
    double sqrt(double x)

# Not a number
isnan = np.isnan
cdef double NaN = <double> np.NaN
cdef double clog2 = log(2.)

# initialize numpy
_import_array()

cdef inline int int_max(int a, int b): return a if a >= b else b
cdef inline int int_min(int a, int b): return a if a >= b else b

# MSVC does not have log2!
cdef inline double Log2(double x):
    return log(x) / clog2

