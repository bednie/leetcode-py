from collections import defaultdict
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def xor(a, b):
            xored = 0
            for i in range(len(a)):
                xored += 1 if (ord(a[i]) ^ ord(b[i])) != 0 else 0
            return xored

        b = defaultdict(list)

        for gene in bank:
            for g in bank:
                if xor(g, gene) == 1:
                    b[gene].append(g)

        dq = [(0, startGene)]
        visited = set()

        while dq:
            edits, gene = dq.pop(0)

            if gene == endGene:
                return edits

            for g in bank:
                if xor(gene, g) == 1 and g not in visited:
                    visited.add(g)
                    dq.append((edits + 1, g))

        return -1
