def gcd(a, b):
    while b != 0:
        d = a % b
        a = b
        b = d
    return a

number = input()
number = int(number)
answers = []

for i in range(number):
    A, B = map(int, input().split(' '))
    answers.append((A*B)//gcd(A,B))

for answer in answers:
    print(answer)
