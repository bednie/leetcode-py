class LRUCache:
    # Definition for doubly-linked list.
    class ListNode:
        def __init__(self, val=0, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

        def __str__(self):
            return f"{id(self)} ListNode[val={self.val}, prev={self.prev}, next={self.next}]"

    def __init__(self, capacity: int):
        self.lookup = {}
        self.capacity = capacity
        self.length = 0
        self.lru = None
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.lookup:
            return self.lookup[key]
            # update lru

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup[key] = value
            # update lru

        else:
            # initialize on first put
            if self.head == None:
                self.head = self.ListNode(val=key, prev=self.ListNode(-999), next=self.ListNode(999))
                self.lru = self.head

            self.length += 1
            self.lookup[key] = value
            
            print(self.head)
            # if length > capacity:
            #   evict lru
            #   update lru


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
