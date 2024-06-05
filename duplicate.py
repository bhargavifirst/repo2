li = ["banana", "banana", "apple", "apple", "kiwi", "orange"]
i = ["banana", "banana", "apple", "apple", "kiwi", "orange"]
li = list(set(li))

print(li)
i = list(dict.fromkeys(i))
print(i)

c = li[2].count("a")
print(c)
s = {100, 20, 10, 10, 40, 70}
sl = dict.fromkeys(s)
print(sl)
sa = len(sl)-1
for j in sl:
    print(sl[sa])
    sa-=1

