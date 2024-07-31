class LRUCache:
    def __init__(self, capacity: int):
        self.lookup = {}
        self.capacity = capacity
        self.length = 0
        self.head = self.ListNode(val=-999)

    # Definition for doubly-linked list.
    class ListNode:
        def __init__(self, val=0, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    def get(self, key: int) -> int:
        if key in self.lookup:
            self.update_cache(key)
            return self.lookup[key]

        return -1

    def put(self, key: int, value: int) -> None:
        # initialize on first put
        if self.head.next == None:
            self.head.next = self.ListNode(val=key, prev=self.head, next=None)
            self.lookup[key] = value

        # update
        self.lookup[key] = value
        self.update_cache(key)

    def update_cache(self, key) -> None:
        # key is already mru
        if self.head.val == key:
            return None

        # key is in cache
        # move to head.next
        node = self.head
        while node:
            if node.val == key:
                if node.next:
                    node.next.prev = node.prev
                node.prev.next = node.next

                if self.head.next:
                    node.next = self.head.next
                    self.head.next.prev = node
                node.prev = self.head
                self.head.next = node
                
                return None

            node = node.next

        # add to cache
        node = self.ListNode(val=key, prev=self.head, next=self.head.next)
        if self.head.next:
            self.head.next.prev = node

        self.head.next = node
        self.length += 1

        if self.length >= self.capacity:
            node = self.head
            while node.next:
                node = node.next
            self.lookup.pop(node.val)
            node.prev.next = None

        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
