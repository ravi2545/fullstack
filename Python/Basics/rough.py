l=[1,4,3,5,7]
n=len(l)
# print(n)
for i in range(n):
    # print(n-i-1)
    # print(i)
    for j in range(0, n-i-1):
        print(l[j],l[j+1])
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]

print(l)

