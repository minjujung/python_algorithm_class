N = input()
N = int(N)

def movie_title(number):    
    if 1 <= number and number <= 10000:
        title =(number - 1) * 1000 + 666
    return print(title)

movie_title(N)