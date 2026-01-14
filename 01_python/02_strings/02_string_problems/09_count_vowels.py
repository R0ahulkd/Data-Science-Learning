a = input("Enter any string : ")
b = "aeiouAEIOU"
sum = 0
for i in b:
    sum += a.count(i)

print(sum)