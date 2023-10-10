def kadanes(arr):
    _sum=float("-inf")
    cs=arr[0]
    n=len(arr)
    for i in range(1,n):
        if cs<0:
            cs=0
        cs=cs+arr[i]
        _sum=max(_sum,cs)

    return _sum
print(kadanes([-3,-2,-19,18,6,-3,15,9,-17,2]))
