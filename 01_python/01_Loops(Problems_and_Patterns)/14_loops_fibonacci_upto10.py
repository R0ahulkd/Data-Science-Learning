a = 0
b = 1
c = 0
n = int(input("Enter a number : "))
if n == 1:
    print(a)
if n == 2:
    print(a)
    print(b)
if n > 2:
    print(a)
    print(b)
    for i in range (0,n-2):
        c = a + b
        a = b
        b = c
        print(c)