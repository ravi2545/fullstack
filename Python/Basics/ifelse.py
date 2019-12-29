# a=1
# b=19
# if(a%2==0):
#     print("Even")
#     if (a > 9):
#         print("your age is {}".format(a))
# else:
#     print("ODD")
#     if (a < 9):
#         print("your age is {}".format(a))

l=[2008,2009]
for year in l:
    if (((year % 4 == 0) and (year % 100 == 0)) or (year % 4 == 0)):
        print("The",year,"is Leap Year")
else:
    print()