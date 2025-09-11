class QueueList:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)
    def is_empty(self):
        return len(self.items) == 0
from collections import deque
class QueueDeque:
    def __init__(self):
        self.items = deque()
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()
    def is_empty(self):
        return not self.items
if __name__ == "__main__":
    q1 = QueueList()
    q1.enqueue("apple")
    q1.enqueue("banana")
    q1.enqueue("cherry")
    print("QueueList dequeue:", q1.dequeue())
    print("QueueList dequeue:", q1.dequeue())
    print("QueueList is empty:", q1.is_empty())
    q2 = QueueDeque()
    q2.enqueue("dog")
    q2.enqueue("elephant")
    q2.enqueue("fox")
    print("QueueDeque dequeue:", q2.dequeue())
    print("QueueDeque dequeue:", q2.dequeue())
    print("QueueDeque is empty:", q2.is_empty())
