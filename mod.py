num1=12345
num2=10
s=0
m=0
while num1!=0:

      m  = int(num1%num2)
      s +=m
      d= int(num1/num2)
      num1=d
print(s)