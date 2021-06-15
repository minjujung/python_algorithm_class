case = input()


def find_room_number(array):
    for i in range(len(array)):
        array[i] = int(array[i])
    room = array[2] // array[0]
    floor = array[2] % array[0]
    if floor == 0:
        floor = array[0]
    else: 
        room += 1
    floor = str(floor)
    if room < 10:
        room = "0" + str(room)
    else:
        room = str(room)
    
    return floor + room
    
answer = []
for i in range(int(case)):
    hotel_info = input().split()
    answer.append(find_room_number(hotel_info))

for i in answer:
    print(i)