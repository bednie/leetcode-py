from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def visit(course: int) -> bool:
            if course in detect_cycle:
                return False

            if course in visited:
                return True

            detect_cycle.add(course)

            for i in digraph[course]:
                if not visit(i):
                    return False

            detect_cycle.remove(course)
            visited[course] = course

            return True
        
        digraph = {}
        for i in range(numCourses):
            digraph[i] = []

        for i in prerequisites:
            digraph[i[0]].append(i[1])

        visited, detect_cycle = {}, set()
        for i in digraph:
            if not visit(i):
                return False

        return True if visited else False