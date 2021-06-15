a, b = input().split()

a = int(a)
b = int(b)

def find_GCD_and_LCM(num1, num2):
    first_num1 = num1
    first_num2 = num2
    if num1 > num2:
        if num1 % num2 == 0:
            gcd = num2
        else:
            while num1 % num2 != 0:
                origin_num1 = num1
                num1 = num2
                num2 = origin_num1 % num2
            gcd = num2
    elif num1 < num2:
        if num2 % num1 == 0:
            gcd = num1
        else:
            while num2 % num1 != 0:
                origin_num2 = num2
                num2 = num1
                num1 = origin_num2 % num1
            gcd = num1
    else:
        gcd = num1
    lcm = int(gcd * (first_num1 / gcd) * (first_num2 / gcd))

    return print(f'{gcd}\n{lcm}')

find_GCD_and_LCM(a, b)