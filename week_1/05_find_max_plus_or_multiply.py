input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    max = 0
    for num in array:
        if num <= 1 or max <= 1:
           max += num
        else:
            max *= num
    return max


result = find_max_plus_or_multiply(input)
print(result)