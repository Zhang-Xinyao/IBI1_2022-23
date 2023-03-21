import numpy as np
import matplotlib.pyplot as plt

N=8
costs=(1,8,15,7,5,14,43,40)
ind=np.arange(N)
width=0.35
p1=plt.bar(ind,costs,width)
plt.ylabel('costs(in $ billions)')
plt.title('Olympic costs in each contury')
plt.xticks(ind,('Los Angeles 1984','Seoul 1988','Barcelona 1992','Atlanta 1996','Sydney 2000','Athens 2003','Beijing 2008','London 2012'))
plt.yticks(np.arange(0,41,5))

plt.show()

costs=[1,8,15,7,5,14,43,40]
print(costs)
