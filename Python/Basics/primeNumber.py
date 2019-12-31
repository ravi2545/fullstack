m=0
flag=0
n=4
m=n/2
if(n==0 or n==1):
    print("NOT A PRIME NUMBER")

else:
    for i in range(2,n):
        if(n%2==0):
            print("Is NOT a prmenumebr")
            flag=1
            break
        if flag==0:
            print("IS PRIME")
