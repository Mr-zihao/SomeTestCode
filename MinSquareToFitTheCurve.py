'''最小二乘法拟合二次曲线'''
 import numpy as np
 import matplotlib.pyplot as plt
 coefficient=np.zeros([3,3])
 right=np.zeros(3)
 samples=[(2,3),(3,2),(4,1),(5,0),(6,1.1),(7,1.9),(8,2.7)]
 plt_x=[]
 plt_y=[]
 for x,y in samples:
     plt_x.append(x)
     plt_y.append(y)
     coefficient[0, 0] += x ** 4
     coefficient[0, 1] += x ** 3
     coefficient[0, 2] += x ** 2
     coefficient[1, 0] += x ** 3
     coefficient[1, 1] += x ** 2
     coefficient[1, 2] += x
     coefficient[2, 0] += x ** 2
     coefficient[2, 1] += x
     coefficient[2, 2] += 1
     right[0]+=y*x**2
     right[1]+=y*x
     right[2]+=y
 solver=np.linalg.solve(coefficient,right)
 plt.figure(1)
 plt.scatter(plt_x,plt_y)
 x_1=np.linspace(1,10,50)
 y_1=np.power(x_1,2)*solver[0]+x_1*solver[1]+solver[2]
 plt.plot(x_1,y_1,'r')
 print(solver)
 plt.show()
'''..................................................'''
