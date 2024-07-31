class LRUCache:
    def __init__(self, capacity: int):
        self.lookup = {}
        self.capacity = capacity
        self.length = 0
        self.head = self.ListNode(val=-999)
        self.tail = self.ListNode(val=-999)
        self.head.next, self.tail.prev = self.tail, self.head

    # Definition for doubly-linked list.
    class ListNode:
        def __init__(self, val=0, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    def get(self, key: int) -> int:

        print("---")
        print("get")
        node = self.head
        while node:
            print(node.val, node.prev, node.next)
            node = node.next
        print("---")

        return -1

    def put(self, key: int, value: int) -> None:
        # initialize on first put
        if self.head.next == None:
            self.head.next = self.ListNode(val=key, prev=self.head, next=self.tail)
            self.lookup[key] = value

        if key not in self.lookup:

            self.length += 1
            self.lookup[key] = value


            # insert in cache
            node = self.head
            while node.next:
                node = node.next

            node.next = self.ListNode(val=key, prev=node, next=None)

            # evict
            # TODO

            # update
            # TODO

        print("---")
        print("put")
        node = self.head
        while node:
            print(id(node), node.val, id(node.prev), id(node.next))
            print("********")
            node = node.next
        print("---")

    def update_cache(self, key) -> None:
        if self.head.val == key:
            return

        node = self.head
        while node:
            if node.val == key:
                node.prev.next = node.next
                node.next.prev = node.prev

                self.head.prev = node
                node.next = self.head
                self.head = node

                return

            node = node.next

        if self.length < self.capacity:
            node = self.ListNode(val=key, prev=None, next=self.head)
            self.head.prev = node
            self.length += 1

            return

        if self.length  self.capacity:
            node = self.ListNode(val=key, prev=None, next=self.head)
            self.head.prev = node
            self.length += 1
            
            return




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
