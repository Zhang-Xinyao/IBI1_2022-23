#To draw a bar plot displaying the sorted distribution 
import numpy as np
import matplotlib.pyplot as plt
#Define the number of horizontal cooridinates
N=8
olympic=['Los Angeles 1984','Seoul 1988','Barcelona 1992','Atlanta 1996','Sydney 2000','Athens 2003','Beijing 2008','London 2012']
costs=[1,8,15,7,5,14,43,40]
#get the list into array to sort the horizontal coordiantes in the order of the size of vertical coordinate
costs=np.array(costs)
olympic=np.array(olympic)
inds=costs.argsort()
sortedolympic=olympic[inds]
ind=np.arange(N)
width=0.35
p1=plt.bar(ind,sorted(costs),width)
plt.ylabel('costs(in $ billions)')
plt.title('Olympic costs in each contury')
#set the coordinate scale
plt.xticks(ind,sortedolympic)
plt.yticks(np.arange(0,41,5))

plt.show()
#output the sorted list of costs
costs=[1,8,15,7,5,14,43,40]
print(sorted(costs))
