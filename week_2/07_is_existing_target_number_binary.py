finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]  # 그냥 이진 탐색을 하면 안됨! 이진 탐색은 정렬이 되어있어야 바로 적용 가능!

# 틀린 코드
def is_exist_target_number_binary(target, numbers):
    current_min = 0
    current_max = len(numbers) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if numbers[current_guess] == target:
            return True
        elif numbers[current_guess] > target:
            current_max = numbers[current_guess] - 1
        else: 
            current_min = numbers[current_guess] + 1
        current_guess = (current_min + current_max) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)