a = [1,5,6,8,2]
b = [4,5,6,7]
c = [1,9,6,2,5]

aset = set(a)
bset = set(b)
cset = set(c)

aset.intersection_update(b)
aset.intersection_update(c)
print(aset)

# 2nd method
print(set(a) & set(b) & set(c))