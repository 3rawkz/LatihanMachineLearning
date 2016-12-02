import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean
import random

def create_dataset(n, variance , step=2 , correlation=False):
    val = 1
    xs = []
    ys = []
    for i in range(n):
        y = val+ random.randrange(-variance,variance)
        ys.append(y)
        if correlation and correlation=='pos':
            val+=step
        elif correlation and correlation=='false':
            val+=step
    xs = [i for i in range(len(ys))]

    return np.array(xs, dtype=np.float64) , np.array(ys, dtype=np.float64)



#return m and b
def bestFitSlope(xs , ys):
    m =  ( (mean(xs) * mean(ys)) - (mean(xs * ys)) ) / ( (mean(xs) * mean(xs) ) - (mean(xs * xs)) )

    b = mean(ys) - m * mean(xs)

    return m,b

def squared_error(ys_origin , ys_line):
    return sum((ys_line - ys_origin)**2)

def coef_determination(ys_origin , ys_line):
    y_mean_line = [ mean(ys_origin) for y in ys_origin ]
    squared_error_regression = squared_error(ys_origin, ys_line)
    squared_error_y_mean = squared_error(ys_origin, y_mean_line)
    return 1 - (squared_error_regression/squared_error_y_mean)

#xs = np.array([1,2,3,4,5,6],dtype=np.float64)
#ys = np.array([5,4,6,5,6,7], dtype=np.float64)

xs, ys = create_dataset(40, 10 , 2 , correlation='pos')


print(ys)

m,b = bestFitSlope(xs,ys)

print('m = ',m,' b = ',b)

x_test = 8
y_test = m*x_test + b

regression_line = [(m * x + b) for x in xs]

r_squared = coef_determination(ys, regression_line)
print('R Squared Value = ',r_squared)

style.use('ggplot')


plt.scatter(xs,ys)
#plt.scatter(x_test,y_test,color="g")
plt.plot(xs,regression_line)
plt.show()
