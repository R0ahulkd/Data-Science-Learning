a = ("OnePlus","Vivo","Redmi")
print(type(a))
a = list(a)
print(type(a)) # It change tuples into list

a.append("Samsung")
a = tuple(a) # After editing data again change to tuples as tuples are immutable
print(type(a))
print(a) 