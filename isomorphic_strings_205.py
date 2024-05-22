from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for i, j in enumerate(s):
            if j not in s_map:
                s_map[j] = [i]
            else:
                s_map[j].append(i)

        for i, j in enumerate(t):
            if j not in t_map:
                t_map[j] = [i]
            else:
                t_map[j].append(i)

        for i, j in zip(s_map, t_map):
            if s_map[i] != t_map[j]:
                return False

        return True


class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = defaultdict(list)
        t_map = defaultdict(list)

        for i in range(len(s)):
            s_map[s[i]].append(i)
            t_map[t[i]].append(i)

            if s_map[s[i]] != t_map[t[i]]:
                return False

        return True
