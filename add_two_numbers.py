# Quick naive implementation for Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1Vals = []
        l2Vals = []
        combinedVals = []
        head = ListNode(0,None)
        tail = head

        # get the values out of l1
        while (l1):
            l1Vals.append(l1.val)
            l1 = l1.next

        # get the values out of l2
        while (l2):
            l2Vals.append(l2.val)
            l2 = l2.next

        # combined the two lists of values
        for i in range(max(len(l1Vals),len(l2Vals))):
            if (i <= len(l1Vals)-1 and i <= len(l2Vals)-1):
                    combinedVals.append((l1Vals[i]+l2Vals[i]))
            elif (i <= len(l1Vals)-1 and i > len(l2Vals)-1):
                    combinedVals.append(l1Vals[i])
            elif (i <= len(l2Vals)-1 and i > len(l1Vals)-1):
                    combinedVals.append(l2Vals[i])

        # make sure each value in combinedVals is less than 10
        for i in range(len(combinedVals)):
            if combinedVals[i] >= 10:
                if i+1 >= len(combinedVals):
                    combinedVals.append(1)
                    combinedVals[i] -= 10
                else:
                    
                    combinedVals[i+1] += 1
                    combinedVals[i] -= 10
            print(combinedVals)

        # add a ListNode for each value in combinedVals
        for i in range(len(combinedVals)):
            tail.next = ListNode(0,None)
            tail = tail.next
            tail.val = combinedVals[i]

        # return ListNode
        return head.next