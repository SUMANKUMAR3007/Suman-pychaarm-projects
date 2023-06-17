a=int(input("enter number:"))
errt=0.01
b=0.0
c=max(1,a)
d=(c+b)/2
while abs(d+d*3-a)>=a:
    if c+c*3<a:
        b=c
    else:
        c=d
        d=(c+b)/2
print("the string is separated into",d," and ",d*3)
