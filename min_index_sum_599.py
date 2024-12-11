from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = {}
        min_idx_sum = 2001
        result = []

        for idx, string in enumerate(list1):
            common[string] = [idx]

        for idx, string in enumerate(list2):
            if string in common:
                common[string].append(idx)
                min_idx_sum = min(sum(common[string]), min_idx_sum)

        for key in common:
            if len(common[key]) > 1 and sum(common[key]) == min_idx_sum:
                result.append(key)

        return result

# test
solution = Solution()
assert solution.findRestaurant(
    ["Shogun", "Tapioca Express", "Burger King", "KFC"],
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
) == ["Shogun"]
