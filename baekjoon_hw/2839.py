inp = int(input())
Box = 0

# 최대한 적은 수의 box를 원하므로 5로 먼저 나눠 보고 
# 나누어 떨어지면 별다른 과정없이 while문을 끝내고 box 갯수 input//5추가
# 5로 안나누어 떨어지면 원래 input에서 3을 빼고 3에 대한 box 갯수 +1을 
# 해준 뒤에 다시 5로 나눠 본다 => 그 과정을 계속하다가 3을 뺐는데 input이
# 0보다 작아지면 `정확하게 N킬로그램을 만들 수 없다`의 의미이므로 -1을 출력한다!!
while True:
    if (inp % 5) == 0:
        Box = Box + (inp//5)
        print(Box)
        break
    inp = inp-3
    Box += 1
    if inp < 0:
        print("-1")
        break