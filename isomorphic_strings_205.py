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
