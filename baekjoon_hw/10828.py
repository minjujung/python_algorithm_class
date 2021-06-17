number = input()
number = int(number)

input_each = []

for i in range(number):
    new_word = input()
    input_each.append(new_word)    

stack = []
def control_stack(string, value):
    if string == "push":
        stack.append(value)
    elif string == "pop":
        if len(stack) == 0:
            return -1
        return stack.pop()
    elif string == "size":
        return len(stack)
    elif string == "empty":
        if len(stack) == 0:
            return 1
        else:
            return 0
    else:
        if len(stack) == 0:
            return -1
        return stack[len(stack) - 1]

answer = []

for i in range(len(input_each)):
    if len(input_each[i]) > 5:
        string_input = input_each[i].split()[0]
        number_input = input_each[i].split()[1]
        result = control_stack(string_input, int(number_input))
    else:
        result = control_stack(input_each[i], 0)
        answer.append(result)

for i in range(len(answer)):
    print(answer[i])
