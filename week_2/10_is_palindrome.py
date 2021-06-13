input = "abcba"


def is_palindrome(string):
    for i in range(len(string)):
        if string[i] == string[(len(string)-1) - i]:
            return True
    return False


print(is_palindrome(input))