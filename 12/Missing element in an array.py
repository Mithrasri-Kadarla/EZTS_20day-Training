#n=int(input("Enter the size:"))#10
#l=list(map(int,input("Enter the array elements:").split()))#2 4 6 1 3 5 8 9

n =10
l = [1,2,3,4,5,6,7,10,9]

c=0
for i in range(1,n+1):#XOR of elements from 1 to max element of an array
    c=c^i
b=0
for i in l:#Xor of elements in an array
    b=b^i
print("Missing Element:",c^b)
