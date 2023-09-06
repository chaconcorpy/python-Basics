# scipy matlib arrays
# import the array from following mat file
from scipy import io
import numpy as np
arr=np.arange(10)
# export the mat file
io.savemat('arr.mat',{'vec':arr})
# import the mat file
mydata=io.loadmat('arr.mat')
# print the mat file in python
print(mydata['vec'])
# in order the show the array in original dimension (1D) use squeeze_me=True( method)
mydata=io.loadmat('arr.mat',squeeze_me=True)
print(mydata['vec'])
# scipy interplotation means the generating points between given points
# e.g;for points 1 & 2, we may interpolate and find points 1.33 and 1.66
# the interp1d() is used to interpolate a distribution with 1 variable.
# it takes x and y points and returns a callable function that can be called with new x and return corresponding y
from scipy.interpolate import interp1d
xs=np.arange(10)
ys=2*xs+1

interp_func=interp1d(xs,ys)
# here the first argument is initial value and 2nd is final and 3rd is interpolate value

newarr=interp_func(np.arange(2.1,3,0.1))
print(newarr)
# spline interpolation: is used instead of interpolate function for a piecewise functions
from scipy.interpolate import UnivariateSpline
yss=xs**2 +np.sin(xs)+1
interp_funct=UnivariateSpline(xs,yss)
newarr1=interp_funct(np.arange(2.1,3,0.1))
print(newarr1)
from scipy.interpolate import Rbf
interp_func=Rbf(xs,yss)
newarr=interp_func(np.arange(2.1,3,0.1))
print(newarr)
# scipy statistical significance tests
from scipy.stats import ttest_ind
v1=np.random.normal(size=100)
v2=np.random.normal(size=100)
res=ttest_ind(v1,v2)
print(res)
# if you want to return only p value ,use the pvalue property
res=ttest_ind(v1,v2).pvalue
print(res)
# ks test is used to check if given value follow a distribution
from scipy.stats import kstest
v=np.random.normal(size=100)
res=kstest(v,'norm')
print(res)
# statistical description of data
# in order to see a summary of values in an array, we can use the describe() function
# it returs:
# mean,variance,skewness,kurtosis,min and max value,num of observation
from scipy.stats import describe
res=describe(v)
print(res)
# normality test to measure the skewness and kurtosis
from scipy.stats import skew,kurtosis
print(skew(v))
print(kurtosis(v))
# find if the data comes from a normal distribution
from scipy.stats import normaltest
print(normaltest(v))
def multipy(x,y):
    return x*y
