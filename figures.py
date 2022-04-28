import numpy as np
from matplotlib import pyplot as plt
x= np.linspace(0,5)

plt.figure()
plt.grid()
# plt.title('Predation Function')
# plt.ylabel('$p(N) = {N^2}/{1+N^2}$')
# plt.xlabel('$N$')
# plt.plot(x,(x**2)/(1+x**2))
# plt.title('Predation Function')
plt.ylabel('$\dot{x}$')
plt.xlabel('$x$')
#k takes values: 3.6, 6.5, 7.5, 20, 30
r,k=0.52,6.5
x_points=[0,0.682 ]
# x_points=[0,1.04,24.92 ]
# x_points=[0,0.8926,1.2551,17.825 ]
# x_points=[0,0.7,2.44,4.35]
y_points=[0,0]
plt.scatter(x_points,y_points, color='black')
plt.plot(x,0*x)
plt.plot(x,r*x*(1-(x/k))-(x**2)/(1+x**2))
plt.show()