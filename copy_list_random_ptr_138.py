from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        map = {}  # original:copy
        node = head
        new_head = new = Node(head.val)

        while node:
            map[node] = new
            node = node.next
            if node:
                new.next = Node(node.val)
                new = new.next

        node = head
        new = new_head
        while node:
            if node.random:
                new.random = map[node.random]
            node = node.next
            new = new.next

        return new_head
