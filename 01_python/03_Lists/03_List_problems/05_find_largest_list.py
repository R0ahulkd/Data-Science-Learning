a = [13,7,12,10]
b = a[0]
for i in range (0,len(a)):
    if b < a[i]:
        b = a[i]

print(b)

# 2nd Method
a.sort()
print(a)
print(a[len(a)-1]) # print(a[-1])