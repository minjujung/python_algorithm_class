
def find_balance(string):
    stack = []
    for i in string:
        if i == "(":
            stack.append("(")
        elif i == "[":
            stack.append("[")
        elif i == ")":
            if len(stack) == 0:
                stack.append(")")
                break
            elif stack[len(stack) - 1] == "[":
                break
            elif stack[len(stack) - 1] == "(":
                stack.pop()
        elif i == "]":
            if len(stack) == 0:
                stack.append("0")
                break
            elif stack[len(stack) - 1] == "(":
                break
            elif stack[len(stack) - 1] == "[":
                stack.pop()
    if len(stack) == 0:
        return "yes"
    else:
        return "no"


answers = []

while True:
    sentence = input()
    if sentence == ".":
        break
    answers.append(find_balance(sentence))

for answer in answers:
    print(answer)