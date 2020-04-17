a=int(input("enter the number :"))
p=0
#z=float(10)
while a//10 >= 0 and a>0:
    p=a%10
    a=a//10
    #print(str(p) +" " + str(z))
    if p%2==1:
        print("The number is odd:" +str(p))
    else:
        print("The number is even:" +str(p))
    #a=z