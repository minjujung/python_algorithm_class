alphabet = input()

croatia_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
replace_number = ["0", "1", "2", "3", "4", "5", "6", "7"]

def how_many_croatia_alphabet(string):
    count = 0
    for i in range(len(croatia_alphabets)):
        if croatia_alphabets[i] in string:
            string = string.replace(croatia_alphabets[i], replace_number[i])
    count += len(string)
    return count

print(how_many_croatia_alphabet(alphabet))

    