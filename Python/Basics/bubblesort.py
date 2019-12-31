# l=[2,3,4,5,6,1,9,8]
# print(len(l))

def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]



arr=[45,3,4,5,66,88,98,3,2]
bubblesort(arr)
print("sorted array is:")
for i in range(len(arr)):
    print(arr[i])