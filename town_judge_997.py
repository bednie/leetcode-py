from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        everyone = set()
        trusts = set()
        trusted_by = set()

        for i in trust:
            everyone.add(i[0])
            everyone.add(i[1])
            trusts.add(i[0])

        if not everyone.difference(trusts):
            return -1

        judge = everyone.difference(trusts).pop()

        for i in trust:
            if i[1] == judge:
                trusted_by.add(i[0])
            
        return judge if len(trusted_by) == n - 1 else -1