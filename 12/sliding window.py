def sliding_window(l,k):# Maximum subarray of given size 
    s=0
    ps=0
    i,j=0,k-1
    while j<len(l):
        if i==0:
            s=sum(l[i:j+1])
            ps=s
        else:
            cs=ps-l[i-1]+l[j]
            s=max(s,cs)
        i+=1
        j+=1
    return s
l=[-3,8,5,2,7,9,-11,18]
k=3
print(sliding_window(l,k))
