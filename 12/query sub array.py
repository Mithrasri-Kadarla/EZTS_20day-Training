def query_subarray_sum(arr,q):
    n=len(arr)
    ps=[0 for i in range(n)]
    for i in range(n):
        if i==0:
            ps[i]=arr[i]
        else:
            ps[i]=ps[i-1]+arr[i]
    for query in q:
        i=query[0]
        j=query[1]
        if i==0:
            print(ps[j],end=" ")
        else:
            print(ps[j]-ps[i-1],end=" ")
l=[3,9,-2,8,7,6,5]
q=[[0,2],[2,5],[3,6]]        
query_subarray_sum(l,q)
