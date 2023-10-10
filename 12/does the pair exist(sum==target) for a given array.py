#arr[i]+arr[i+1]=target     target-arr[i+1]=arr[i]
def is_pair_exist(arr,target):
    pairs=set()
    pairs2=set()
    c=0
    for i in arr:
        j=target-i
        if j in pairs:
            c+=1
            pairs2.add((i,j))
        pairs.add(i)
    if c>0:
        print("True")
    else:
        print("False")
    return c,pairs2
arr=[-3,8,7,2,-5,13,18,9,6]
target=int(input())
x=is_pair_exist(arr,target)
print(x)
