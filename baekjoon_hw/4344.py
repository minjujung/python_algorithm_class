case = input()

percent_array = []

for i in range(int(case)):
    numbers_scores = [x for x in input().split()]
    students_num = int(numbers_scores[0])
    sum = 0
    count = 0
    if 1 <= students_num and students_num <= 1000:
        for j in range(1,  len(numbers_scores)):
            sum += int(numbers_scores[j])
        average = sum / students_num
        for j in range(1, len(numbers_scores)):
            if average < int(numbers_scores[j]):
                count += 1
        percent = count / students_num * 100
        percent_array.append("{:.3f}%".format(percent))

for answer in percent_array:
    print(answer)
    

        

