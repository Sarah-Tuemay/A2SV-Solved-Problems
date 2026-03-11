class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.front = None
        self.rear = None
        self.max_size = k
        self.queue_size = 0

    def insertFront(self, value: int) -> bool:
        if self.queue_size == self.max_size:
            return False

        new_node = Node(value)
        if self.front == None:
            self.front = new_node
            self.rear = new_node
        else:
            self.front.prev = new_node
            new_node.next = self.front
            self.front = new_node

        
        self.queue_size +=1
        return True
            
    def insertLast(self, value: int) -> bool:
        if self.queue_size == self.max_size:
            return False
        
        new_node = Node(value)

        if self.rear == None:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node


        self.queue_size +=1

        return True

    def deleteFront(self) -> bool:
        if self.front == None:            
            return False
        
        self.front = self.front.next
        
        

        self.queue_size -= 1

        if self.queue_size == 0:
            self.rear = None
        else:
            self.front.prev = None
        return True
        
    def deleteLast(self) -> bool:
        if self.rear == None:
            return False

        self.rear = self.rear.prev
        self.queue_size -= 1

        if self.queue_size == 0:
            self.front = None
        else:
            self.rear.next = None
            
        return True

    def getFront(self) -> int:
        if self.front:
            return self.front.val
        
        return -1

    def getRear(self) -> int:
        if self.rear:
            return self.rear.val
        
        return -1

    def isEmpty(self) -> bool:
        return self.queue_size == 0

    def isFull(self) -> bool:
        return self.queue_size == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()