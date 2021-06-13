class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
first_node = Node(4)
node.next = first_node
print(node.next.data)

# LinkedList class는 head node만 가지고 있으면 된다
class LinkedList:
    def __init__(self, data):
        self.head = Node(data) 

    # None 이 나올때 까지 head를 옮겨줘야 일일히 linked_list.next = LinkedList(3)처럼
    # 연결 시켜주지 않아도 자동으로 맨뒤에 새로운 node가 추가된다
    # [3] -> [4] -> [5] -> [6] -> Node
    def append(self, data):

        # None
        # 위의 주석처럼 head자체가 none인 경우도 있다
        # 이 경우는 결국 None뒤에 새로운 Node를 붙이는 게 
        # 새로운 head를 만드는 것과 동일하다!
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next # [3] -> [4]
                           #        cur
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()
