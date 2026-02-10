import pandas as pd
import random as rnd
import numpy as np
mydataset = {
  "kocka1": [],
  'kocka2': [] ,
 "kocka3":[],
}
for j in mydataset.keys():
    for i in range(20):
        h=rnd.randint(1,6)
        mydataset[j].append(h)

f=[]
g=[]
for i in range(20):
    q1=mydataset["kocka1"][i]
    q2=mydataset["kocka2"][i]
    q3=mydataset["kocka3"][i]
    f.append(q1+q2+q3)
    g.append(q1*q2)
mydataset["sum"]=f
mydataset["sucin"]=g
myvar = pd.DataFrame(mydataset)

print(myvar)