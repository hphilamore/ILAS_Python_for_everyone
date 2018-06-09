# Test-Yourself Exercise: Curve Fitting
import numpy as np
import matplotlib.pyplot as plt
A = np.loadtxt('sample_data/signal_data.csv',dtype=float,delimiter="\t")
x = A[0]
y = A[1]

def function1(x, a, b):
    y = a * np.sin(x+b) 
    return y

from scipy.optimize import curve_fit

opt, cov = curve_fit(function1, x, y)

y_fit = function1(x, *opt)

def RMSE(raw, fitted):
    e = (fitted - raw)
    return np.sqrt(np.sum(e**2)/ len(y))

rmse = RMSE(y_fit, y)

plt.plot(x, y,'o',label='raw data')
plt.plot(x,y_fit,label='fitted data')
plt.legend(loc='best')
plt.title('RMSE: {rmse}')

print(f"y = {opt[0]} * e**({opt[1]}*x)")
plt.savefig("img/my-plot.pdf")


# Test-yourself Exercise: Interpolation
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splrep
from scipy.interpolate import splev
import scipy.interpolate

# original data
x = np.array([19.1,19.1,19,18.8,18.7,18.3,18.2,17.6,11.7,9.9,9.1])
y = np.array([0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10])


# range of values for x axis
plt.xlim(x[9], x[20]);

# order polynomial interpolation
x_fit1 = scipy.interpolate.interp1d(y,x)


# plot labels and legend
plt.xlabel('Temperature')
plt.ylabel('Depth')
plt.legend(loc='best', fontsize=12)

plt.plot(x_fit1,y)