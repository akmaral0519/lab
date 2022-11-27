a = input()
d = 0
for i in range(len(a)):
    d += int(a[i]) * (2 ** (len(a) - i - 1)) 
print(d)


