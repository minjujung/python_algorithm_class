word_num = input()

def group_word(string):
    arr = []
    for i in range(len(string)):
        if i <= 1:
            arr.append(string[i])
        elif i > 1:
            if string[i] in arr and arr[len(arr) - 1] != string[i]:
                return False
            else:
                arr.append(string[i])
                continue
    else:
        return True

count = 0
                
for i in range(int(word_num)):
    string_input = input()
    if group_word(string_input):
        count += 1
print(count)
