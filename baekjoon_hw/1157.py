word = input()

def find_max_occurred_alphabet(string):
    if len(string) <= 1000000:
        alphabet_occurence_array = [0] * 26
        for alphabet in string:
            if ord(alphabet) < 97:
                alphabet_occurence_array[ord(alphabet) - ord("A")] += 1
            else:
                alphabet_occurence_array[ord(alphabet) - ord("a")] += 1

        max_occurrence = 0
        max_alphabet_occurrence = 0

        for index in range(len(alphabet_occurence_array)):
            alphabet_occurence = alphabet_occurence_array[index]

            if alphabet_occurence > max_occurrence:
                max_alphabet_index = index
                max_occurrence = alphabet_occurence
        count = 0
        for i in alphabet_occurence_array:
            if max_occurrence == i:
                count += 1
        if count > 1:
            return "?"
        else:
            return chr(max_alphabet_index + ord('A'))


print(find_max_occurred_alphabet(word))
