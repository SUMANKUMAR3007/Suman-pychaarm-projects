h=int(input('enter the length of the string'))
errt=0.01
r=0
while errt<=abs(r+r*3-h) and r<=h:
    r=r+errt
if(abs(r+r*3-h)>=errt):
    print("sorry failed to find approximate solution")
else:
    print("the approximate separation of the string is as ",r," and ",r*3)


