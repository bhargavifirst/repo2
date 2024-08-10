s= ['a', 10, 4, 5, 'c', 'd']
l=[]
z=[]
for i in s:
    if isinstance(i,int):
        l.append(i)
    else:
        z.append(i)
print(l)
print(z)

