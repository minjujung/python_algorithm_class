input = "(())()"


def is_correct_parenthesis(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


print(is_correct_parenthesis(input))  # True 를 반환해야 합니다!