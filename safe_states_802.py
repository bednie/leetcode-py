from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def visit(state: int) -> bool:
            if state in detect_cycle:
                return False

            if state in safe:
                return True

            detect_cycle.add(state)

            for s in digraph[state]:
                if not visit(s):
                    return False

            detect_cycle.remove(state)
            safe[state] = state

            return True

        digraph = {}
        for i in range(len(graph)):
            digraph[i] = graph[i]

        result, safe, detect_cycle = [], {}, set()
        for i in digraph:
            if visit(i):
                result.append(i)

        return result
