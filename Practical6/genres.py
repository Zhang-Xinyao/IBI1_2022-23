#use metplotlib to draw a pie chart
#each fraction of the pie chart is defined by the labels and percentage(represented by size)
#design the fraction of the radius with which to offset each wedge
import matplotlib.pyplot as plt

labels='comedy','action','romance','fantasy','science-fiction','horror','crime','documentary','history','war'
sizes=[73,42,38,28,22,19,18,12,8,7]
explode=(0.1,0,0,0,0,0,0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
#ensure the pie is drawn as a circle
plt.axis('equal')
plt.show()

#make a dictionary containing the information about the students' favourite movie gernes
genre={'Comedy':73,'Action':42,'Romance':38,'Fantasy':28,'Science-fiction':22,'Horror':19,'Crime':18,'Documentary':12,'History':8,'War':7}
#input the variable"Comedy" and output the number of students
imput='Comedy'
print(genre[imput])

