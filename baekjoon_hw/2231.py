
number = input()
number = int(number)

sum = 0
answer_list = []
for i in range(1, number):
    sum += i
    str_number = str(i)
    for j in range(len(str_number)):
        sum += int(str_number[j])
    if sum == number:
        answer_list.append(i)
    sum = 0

if len(answer_list) == 0:
    answer = 0
else:
    answer = min(answer_list)

print(answer)