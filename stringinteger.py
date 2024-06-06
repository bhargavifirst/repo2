

s="bhar123gavi"
t=""
n=""
h=len(s)-1
i=-1
while i<h:
   i = i + 1
   if (s[i]).isdigit():
      t +=s[i]
   else :
       n +=s[i]

print(t)
print(n)