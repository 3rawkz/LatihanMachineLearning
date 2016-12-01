import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean

def bestFitSlope(xs , ys):
    m =  ( (mean(xs) * mean(ys)) - (mean(xs * ys)) ) / ( (mean(xs) * mean(xs) ) - (mean(xs * xs)) )

    b = mean(ys) - m * mean(xs)

    return m,b

xs = np.array([1,2,3,4,5,6],dtype=np.float64)
ys = np.array([5,4,6,5,6,7], dtype=np.float64)

m,b = bestFitSlope(xs,ys)

print(m,b)

x_test = 8
y_test = m*x_test + b

regression_line = [(m * x + b) for x in xs]

style.use('ggplot')

plt.scatter(xs,ys)
plt.scatter(x_test,y_test,color="g")
plt.plot(xs,regression_line)
plt.show()
