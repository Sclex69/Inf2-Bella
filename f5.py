from os import replace
c=0
f = open("c.txt")

f=f.readlines()

for i in f:
    i = i.rstrip()
    v=max(i)
    g=i.index(v)
    print(len (i))
    if g== (len(i)-1):
        v2=v
        i = i.replace(v, "0", 1)
        v=max(i)
    else:
        i = i[g:]
        i=i.replace(v,"0",1)

        v2 = max(i)



    r = v + v2
    print(r)
    c=int(r)+c
    print(c)
print(c)