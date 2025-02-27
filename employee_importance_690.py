from typing import List

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        for emp in employees:
            if emp.id == id:
                return emp.importance + sum([self.getImportance(employees, i) for i in emp.subordinates])
                

# test 
s = Solution()
e1 = Employee(1, 5, [2,3])
e2 = Employee(2, 3, [])
e3 =  Employee(3, 3, [])
e = [e1, e2, e3]
assert s.getImportance(e, 1) == 11