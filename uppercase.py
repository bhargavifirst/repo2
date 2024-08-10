a = "assforrc"
k = len(a) - 1
#identifying duplicates
for i in range(k):
    n = k  # Reset n to the last index in each iteration of i
    while n > i:
        if a[i] == a[n]:

            print(f"Match found: {a[i]} at positions {i} and {n}")
            break
        n -= 1


















