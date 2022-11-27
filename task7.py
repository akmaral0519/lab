def election(x:bool, y:bool, z:bool):
    if x+y+z > 1:
        return 1
    else:
        return 0

a = input().split()
print(election(bool(int(a[0])), bool(int(a[1])), bool(int(a[2]))))