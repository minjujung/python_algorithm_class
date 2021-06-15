number = input()
number = int(number)

divisor = input().split()

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j  in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return

def find_number_from_real_divisor(number, list):
    if number == 1:
        return print(int(list[0])**2)
    for i in range(len(list)):
        list[i] = int(list[i])
    insertion_sort(list)
    return print(list[0] * list[len(list) - 1])

find_number_from_real_divisor(number, divisor)


