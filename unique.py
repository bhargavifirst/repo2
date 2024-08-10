l = [10, 20, 20, 30, 40, 10]
i=0
while i < len(l):
    j = i + 1
    while j < len(l):
        if l[i] == l[j]:
            del l[j]
        j += 1
    i +=1
print(l)
