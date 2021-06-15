number = input()
number = int(number)

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, to_pos)
        return

    hanoi(n - 1, from_pos, aux_pos, to_pos)
    print(from_pos, to_pos)
    hanoi(n - 1, aux_pos, to_pos, from_pos)

# 횟수는 왜 이렇지..?
print(2**number -1)
hanoi(number, 1, 3, 2)
