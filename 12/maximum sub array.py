def max_subarr(arr):
    ms=arr[0]
    cs=arr[0]
    for i in arr[1:]:
        print(i)
        cs=max(i,cs+i)
        print(ms)
        ms=max(ms,cs)
        print(ms)
    return ms
arr=[1,2,3,-4]
x=max_subarr(arr)
print(x)
