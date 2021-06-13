input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for alphabet in string:
        if not alphabet.isalpha():
            continue
        arr_index = ord(alphabet) - ord('a')
        alphabet_occurrence_array[arr_index] += 1 
    
    not_repeating_charater_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_charater_array.append(chr(index + ord("a")))
    for char in string:
        if char in not_repeating_charater_array:
            return char
    return "_"

                
                

result = find_not_repeating_character(input)
print(result)