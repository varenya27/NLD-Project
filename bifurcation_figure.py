import numpy as np
from matplotlib import pyplot as plt
kplot = list(range(3,34))
# print(kplot)
x=[[0, 0.55413], [0, 0.60173], [0, 0.63853], [0, 0.66861], [0, 0.69414], [0, 0.71643, 2.19397, 5.0896], [0, 0.73632, 1.92977, 6.33391], [0, 0.75436, 1.77426, 7.47137], [0, 0.77099, 1.66621, 8.56281], [0, 0.7865, 1.58455, 
9.62896], [0, 0.80113, 1.51948, 10.67939], [0, 0.81507, 1.46566, 11.71927], [0, 0.82849, 1.41982, 12.75168], [0, 0.84154, 1.37988, 13.77858], [0, 
0.85434, 1.34437, 14.80129], [0, 0.86702, 1.31225, 15.82073], [0, 0.87973, 1.2827, 16.83757], [0, 0.89263, 1.25506, 17.85231], [0, 0.9059, 1.22878, 18.86532], [0, 0.91982, 1.20329, 19.87689], [0, 0.93479, 1.17796, 20.88725], [0, 0.95153, 1.15189, 21.89658], [0, 0.97155, 1.12343, 22.90502], [0, 1.0, 1.08729, 23.91271], [0, 24.91974], [0, 25.92618], [0, 26.93212], 
[0, 27.9376], [0, 28.94268], [0, 29.9474]]
p1,p2,p3,p4=[],[],[],[]
flag=0
for lis in x:
    if len(lis)==4:
        flag=1
    if flag==1 and lis==2:
        flag=2
    if flag==0:
        p1.append(lis[0])
        p2.append(lis[1])
    if flag==1 and len(lis)==4:
        p1.append(lis[0])
        p2.append(lis[1])
        p3.append(lis[2])
        p4.append(lis[3])

    if flag==2:
        p1.append(lis[0])
        p4.append(lis[1])
# print(len(x))
print(p1)
print(p2)
print(p3)
print(p4)
plt.figure()
xp1=list(range(0,len(p1)))
xp2=list(range(0,len(p2)))
xp3=list(range(0,len(p3)))
xp4=list(range(0,len(p4)))
plt.plot(xp1,p1,'--')
plt.plot(xp2,p2,'-')
plt.plot(xp3,p3,'--')
plt.plot(xp4,p4,'-')
plt.grid()
plt.xlabel('$k$')
plt.ylabel('$x$')
i=0
# for set in x:
#     for point in set:
#         plt.scatter(kplot[i], point,color='black',s=5)
#     i+=1
plt.show()