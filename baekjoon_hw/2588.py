a = input()
b = input()

a = int(a)

for i in range(len(b) - 1, -1, -1):
    print(a*int(b[i]))

print(a*int(b))