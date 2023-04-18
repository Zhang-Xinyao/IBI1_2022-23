class triathlon(object):
#define a class as "triathlon"
    def __init__(self,first_name,last_name,location,swim,cycle,run,total):
        #the data are attributed to the person's first name, last name, competition location, swim time, cycle time, run time and total time for triathlon
        self.a=first_name
        self.b=last_name
        self.c=location
        self.d=swim
        self.e=cycle
        self.f=run
        self.g=total

#the example
x=triathlon('Hua','Li','Beijing','20 min','60 min','30 min','110min')
print(x.a,x.b,x.c,x.d,x.e,x.f,x.g)
