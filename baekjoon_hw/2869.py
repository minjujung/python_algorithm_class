daytime, night, days = input().split()

daytime = int(daytime)
night = int(night)
days = int(days)

def how_many_days_needed(num1, num2, num3):
    n = (num3 - num2) // (num1 - num2)
    if (num3 - num2) % (num1 - num2) != 0:
        n += 1
    return print(n)

how_many_days_needed(daytime, night, days)