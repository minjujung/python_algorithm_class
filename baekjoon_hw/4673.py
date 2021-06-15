def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j  in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return array

def self_number(num):
    number_array = []
    not_self_numbers = []
    for i in range(num):
        number_array.append(str(i + 1))
        sum = 0
        for j in range(len(number_array[i])):
            sum += int(number_array[i][j])
        total_sum = sum + int(number_array[i])
        if total_sum <= num:
            not_self_numbers.append(str(total_sum))
    num_set = set(number_array)
    not_self_num_set = set(not_self_numbers)
    self_num = list(num_set - not_self_num_set)

    self_real_num = []
    for number in self_num:
        self_real_num.append(int(number))
    self_real_num = insertion_sort(self_real_num)
        
    for each_self_num in self_real_num:
        print(each_self_num)

self_number(10000)