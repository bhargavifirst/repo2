num1=235
num2=10
s=0
m=0
while num1!=0:
      s = (s * 10)
      m  = int(num1%num2)
      s +=m
      
      d= int(num1/num2)
      num1=d

      print(s)