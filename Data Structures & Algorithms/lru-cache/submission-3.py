class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.dct = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.dct:
            node = self.dct[key]
            self._remove(node)
            self.add_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            node = self.dct[key]
            node.val = value
            self._remove(node)
            self.add_front(node)
        else:
            self.dct[key] = Node(key, value)
            self.add_front(self.dct[key])
            if len(self.dct) > self.capacity:
                node = self.tail.prev
                self._remove(self.tail.prev)
                self.dct.pop(node.key)
   
            
        
