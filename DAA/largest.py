x=int(input("Enter first No."))
y=int(input("Enter second No."))
z=int(input("Enter third No."))
if(x>>y&x>>z):
    print(x)
elif(y>>x&y>>z):
    print(y)
elif(z>>x&z>>y):
    print(z)