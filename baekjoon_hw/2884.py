a,b = input().split()

a = int(a)
b = int(b)

if 0 <= b and b <= 59:
    if 0 <= a and a <= 23:
        if b < 45:
            b += 15
            if a - 1 < 0:
                a += 23
            else:
                a -= 1
        else:
            b -= 45

print(a, b)