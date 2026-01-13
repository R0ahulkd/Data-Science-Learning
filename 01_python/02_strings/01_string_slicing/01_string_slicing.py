a = "Harry Potter and the Goblet of fire"
b = "0123456789"
print(a[0:5]) #  Print Harry index 0 to 4
print(a[6:12])
print(a[:5])
print(a[-4:]) # To start from backside it prints fire

print(b[::2]) # 3rd value defines steps now it prints after skip values 02468
print(b[1:8:2])
print(b[::-1]) # it reverse the string starting from end
# [starting value:end value:step]