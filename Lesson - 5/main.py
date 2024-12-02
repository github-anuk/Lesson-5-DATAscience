import matplotlib.pyplot as mp
import numpy as np

#CREATE GRAPH

x=[1,2,3,4,5]
y=[1,2,3,4,5]

#mp.plot(x,y,"ro")
#mp.plot(x,y,"g^")
#mp.plot(x,y,"r--")
#mp.plot(x,y,"b--")
mp.plot(x,y,"b-")
mp.axis([0,10,0,200])
mp.show()

mp.plot(x,y,"g--",label="Y=X",linewidth = 4)
mp.axis([0,10,0,50])
mp.xlabel("Y AIXISS")
mp.ylabel("X AXISSS FOR SURE")
mp.title("Sample Graph")
mp.legend()
mp.show()

x=np.arange(1,10,0.2)
print(x)
ysquare=x**2
ycube=x**3

mp.plot(x,ysquare,"r--",x,ycube,"b--")
mp.show()

#TESK ONEH -- PLOT THE LINE Y = MX=C using matplotlib

m=2
c=1

x=np.linspace(-5,5,100)

y=m*x+c

mp.plot(x,y,"r--")
mp.xlabel("Y ASIS NOT X AXIS FOR SURE")
mp.ylabel("X AXIS AND NOT Y AXIS FOR SURE :)")
mp.title("GRAPH FOR LINEAR THING")
mp.legend()
mp.show()

#BAR GRAPHH
#X AXIXS=position of bar
#Y AXISX=LENGTH OF BAR

mp.bar([1,3,5,7],[2,4,6,8], color = "b")
mp.show()

mp.bar([1,3,5,7],[2,4,6,8], color = "b")
mp.bar([2,4,6,8],[3,4,8,6],color ="r")
mp.show()

#SHOWING CATOGRIAL DATA USING BAR PLOT
mp.bar(["Male Litercay","Femal Literacy"],[90,95])
mp.show()

mp.bar(["economy","economy plus","business","first","residence"],[200,75,25,10,5])
mp.show()