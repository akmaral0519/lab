def double_power(a:float, n:int):
    return a ** n

a = input().split()
print(double_power(float(a[0]),int(a[1])))
