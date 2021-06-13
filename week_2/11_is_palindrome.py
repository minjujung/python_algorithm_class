input = "소주만병만주소"

#축소되면서 반복될때 재귀함수 사용!
def is_palindrome(string):
    if len(string) <= 1:
        return True
        
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


print(is_palindrome(input))