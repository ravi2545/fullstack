# for i in range(1,4):
#     for j in range(1,4):
#         if i==j:
#             print(i,j)
#


for i in range(1,6):
    for j in range(1,i+1):
        print("* ", end="")
    print("\r")


for num in range(10):
    for x in range(num):
        print(num,end=" ")
    print("")