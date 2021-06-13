class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # enqueue(data) : 맨 뒤에 데이터 추가하기 
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node  
        self.tail = new_node

    # dequeue() : 맨 앞의 데이터 뽑기
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        dequeue_head = self.head
        self.head = self.head.next
        return dequeue_head.data

    # peek() : 맨 앞의 데이터 보기
    def peek(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.head.data

    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())