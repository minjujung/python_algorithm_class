import sys
input = sys.stdin.readline

number = int(input())
queue = []
count = 0

for i in range(number):
    comm = input().strip()
    string = comm.split()[0]
    if string == "push":
        queue.append(comm.split()[1])
    elif string == "pop":
        if len(queue) - count == 0:
            print(-1)
        else:
            print(queue[count])
            count += 1
    elif string == "size":
        print(len(queue) - count)
    elif string == "empty":
        if len(queue) - count == 0: 
            print(1)
        else:
            print(0)
    elif string == "front":
        if len(queue) - count == 0:
            print(-1)
        else:
            print(queue[count])
    else:
        if len(queue) - count == 0:
            print(-1)
        else:
            print(queue[-1])



