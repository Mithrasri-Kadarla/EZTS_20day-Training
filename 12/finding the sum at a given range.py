l=[3,9,-2,8,7,6,5]
s=0
sl=[]
for i,j in enumerate(l):
    s+=j
    sl.append(s)
    print(i,s)
print(sl)
r=sl[5]-sl[2]
print(r)
