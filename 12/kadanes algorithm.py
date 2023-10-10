def kadanes(arr):
    s=float('-inf')
    cs=arr[0]
    n=len(arr)
    for i in range(1,n):
        if cs<0:
            cs=0
        cs+=arr[i]
        if arr[i]<0:
            s=max(s,cs+arr[i])
    return max(s,cs)
l=[-3,-2,-19,18,6,-3,15,9,-17,2]
print(kadanes(l))
