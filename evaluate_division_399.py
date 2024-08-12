from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        def search(query: List[str], path: list):
            self.visited[query[0]] = True

            if query[0] == query[1]:
                self.paths.append(path)
                self.res = True
                return

            for v in self.edges[query[0]]:
                if v not in self.visited:
                    search([v, query[1]], path + [v])

        vals = {}
        self.edges = defaultdict(list)
        self.paths = []
        self.visited = {}
        results = []

        # build graph edges and vertices
        for e, v in zip(equations, values):
            e0, e1 = e
            self.edges[e0].append(e1)
            self.edges[e1].append(e0)
            vals[(e0, e1)] = v
            vals[(e1, e0)] = 1 / v

        # evaluate query
        for q in queries:
            if q[0] not in self.edges or q[1] not in self.edges:
                self.paths.append(None)
                continue

            self.res = False
            search(q, [q[0]])
            if not self.res:
                self.paths.append(None)
            self.visited.clear()

        # compute product of path
        for path in self.paths:
            if path is None:
                results.append(-1.0)

            elif len(path) == 1:
                results.append(1.0)

            else:
                ans = 1.0
                for i in range(len(path) - 1):
                    ans *= vals[path[i], path[i + 1]]
                results.append(ans)

        return results
