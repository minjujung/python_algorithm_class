class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    # index번째 node 불러오기
    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    # index 번째에 새로운 원소값 추가
    def add_node(self, index, value):
        new_node = Node(value)  # 새로운 node만드는 과정
        if index == 0:       
            new_node.next = self.head
            self.head = new_node
        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
print(linked_list.get_node(1).data) # -> 5를 들고 있는 노드를 반환해야 합니다!

print("모든 node의 data value출력")
linked_list.add_node(1, 6)
linked_list.print_all()