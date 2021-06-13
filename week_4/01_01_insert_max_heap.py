class MaxHeap:
    def __init__(self):
        self.items = [None]
        
    # 1. 원소를 맨 끝에 추가
    # 2. 지금 넣은 새 노드를 부모와 비교, 부모보다 크면 교체
    # 3. 이 과정을 꼭대기까지 반복
    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:
            parent_index = cur_index // 2
            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!