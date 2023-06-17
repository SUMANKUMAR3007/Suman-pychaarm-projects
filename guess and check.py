n=int(input ("please enter the length of your string:"))
k=0
while k<=n:
      if k+k*3>=abs(n):
         break
      k+=1
      if k+k*3==abs(n):
          print("therefore,the two string are,k,"and ",k*3")
      else:
          print("hence ,the string be aplitted into halfs such that one half is there times the other half")
