from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd

#import the file "go_obo.xml"
DOMTree=xml.dom.minidom.parse("go_obo.xml")
collection=DOMTree.documentElement
terms=collection.getElementsByTagName('term')

#make empty lists to store the data
id_list=[]
name_list=[]
defstr_list=[]
is_a_list=[]

#define a function that can use recursion to count the childnodes of a specific id
#use for loop to count the childnodes 
#find the first childnode of is_a and identify if it equals to id
#keep recursion to count every childnodes
def count_childnodes(id):
    count=0
    for term in terms:
        is_as=term.getElementsByTagName('is_a')
        for is_a in is_as:
            if is_a.firstChild.data==id:
                count+=1
                count+=count_childnodes(term.getElementsByTagName('id') [0].firstChild.data)
    return count

#extract the data from GO id, name, definition and childnodes number
#put the data into dictionary firstly
#convert the dictionary into dataframe       
for term in terms:
    id=term.getElementsByTagName('id')[0]
    name=term.getElementsByTagName('name')[0]
    defstr=term.getElementsByTagName('defstr')[0]
    if 'autophagosome' in defstr.childNodes[0].data:
        id_list.append(id.childNodes[0].data)
        name_list.append(name.childNodes[0].data)
        defstr_list.append(defstr.childNodes[0].data)
        is_a_list.append(count_childnodes(id.childNodes[0].data))
all_dict={'id':id_list,'name':name_list,'definition':defstr_list,'childnodes':is_a_list}
df=pd.DataFrame(all_dict)
#get the file "autophagosome.xlsx"
df.to_excel('autophagosome.xlsx',index=False)
