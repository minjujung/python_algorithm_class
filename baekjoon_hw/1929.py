a, b = input().split()

a = int(a)
b = int(b)

def prime_list(n):
    sieve = [True] * n
    m = int(n**0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i*i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

li = prime_list(b + 1)
answers = [i for i in li if i >= a]

for answer in answers:
    print(answer)