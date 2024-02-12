#
# Stars of Scientific Computing, March 5 2017
# Checks to make sure you have the correct dependencies installed
#

import os
from subprocess import check_call,CalledProcessError
import numpy
import scipy
from scipy import stats
import matplotlib.pyplot as plt

pyversion = sys.version_info.major  
assert (pyversion == 3), "You have Python "+str(pyversion)+" installed. Please install Python 3.x."
nversion = np.version.version
assert (nversion >= 1.12), "You have NumPy "+str(nversion)+" installed. Please install NumPy 1.12 or above."
sversion = scipy.version.version
assert (sversion >= 0.18), "You have SciPy "+str(sversion)+" installed. Please install SciPy version 0.18 or above."
try:
    jversion = check_call(["which", "jupyter"])
except CalledProcessError:
    print("You do not have Jupyter notebook installed. Please install Jupyter notebook.")
