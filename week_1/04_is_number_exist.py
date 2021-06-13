input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for num in array:               #array 길이 만큼 아래 연산 실행
        if num == number:           #비교연산 1번 실행
            return True             #N * 1 = N 번 만큼 실행
    return False

result = is_number_exist(3, input)
print(result)