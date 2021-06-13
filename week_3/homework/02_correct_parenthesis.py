s = "(())()"


def is_correct_parenthesis(string):
    left = 0
    right = 0
    for char in s:
        if char == "(":
            left += 1
        else:
            right += 1
    if left != right:
        return False
    else: 



print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!