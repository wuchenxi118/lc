# import collections
#
# class LRUCache(collections.OrderedDict):
#
#     def __init__(self, capacity: int):
#         super().__init__()
#         self.capacity = capacity
#
#
#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         self.move_to_end(key)
#         return self[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last=False)

class ListNode():
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoubleList():
    def __init__(self):
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addFirst(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size+=1

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size-=1

    def removeLast(self):
        if self.tail.prev == self.head:
            return None
        last = self.tail.prev
        self.remove(last)
        return last

    def getSize(self):
        return self.size

class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.cache = DoubleList()
        self.cap = capacity


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        val = self.map[key].value
        self.put(key,val)
        return val


    def put(self, key: int, value: int) -> None:
        x = ListNode(key=key,value=value)
        if key in self.map:
            self.cache.remove(self.map[key])
            self.cache.addFirst(x)
            self.map[key] = x
        else:
            if self.cap == self.cache.getSize():
                last = self.cache.removeLast()
                self.map.pop(last.key)
            self.cache.addFirst(x)
            self.map[key] = x





if __name__ == '__main__':

    LRU = LRUCache(2)
    LRU.put(2,1)
    LRU.put(1,1)
    LRU.get(2)
    LRU.put(4,1)
    LRU.get(1)
    LRU.get(2)

