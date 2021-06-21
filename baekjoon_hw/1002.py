import sys

input = sys.stdin.readline

case = int(input())
answer = []


#이렇게 조건대로 구문을 나눌 때는 조건의 순서 잘 따지기!!
# 적게 나오는 경우 부터 시작해야함
# 예를 들어 distance_2 = 0인경우는 `반지름의 차나 합과 같을 때`에 포함 될수 있기 때문...
for i in range(case):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    distance_2 = (x2 - x1)**2 + (y2 - y1)**2
    if distance_2 == 0 and r1 == r2:
        answer.append(-1)
    elif distance_2 == (r1 + r2)**2 or distance_2 == (r1 - r2)**2:
        answer.append(1)
    elif (r1 - r2)**2 < distance_2 and distance_2 < (r1 + r2)**2:
        answer.append(2)
    else:
        answer.append(0)

for i in answer:
    print(i)


