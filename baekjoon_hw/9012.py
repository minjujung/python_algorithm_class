number = input()
number = int(number)

answers = []
for i in range(number):
    stack = []
    parenthis = input()
    for j in range(len(parenthis)):
        if parenthis[j] == "(":
            stack.append("(")
        elif parenthis[j] == ")":
            if len(stack) == 0:
                stack.append(")")
                break
            else:
                stack.pop()
    if len(stack) == 0:
        answers.append("YES")
    else:
        answers.append("NO")

for answer in answers:
    print(answer)