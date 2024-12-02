import numpy as np 
import matplotlib.pyplot as mp
choice=int(input("PLEASE CHOSE OPTION 1 -- LINEAR OR OPTION 2 -- QUADRATIC"))
a=int(input("START VALUEEE"))
b=int(input("ED VALUE"))
x=mp.linspace(a,b,1)
m=2
c=1
if choice==1:
    y=m*x+c
    mp.