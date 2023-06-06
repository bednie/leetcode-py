import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from median_of_two_sorted_arrays import Solution

def test_findMedianSortedArrays():
    sol = Solution()
    
    # Test case 1: Odd number of elements
    nums1 = [1, 2, 3]
    nums2 = [4, 5]
    assert sol.findMedianSortedArrays(nums1, nums2) == 3.0

    # Test case 2: Even number of elements
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert sol.findMedianSortedArrays(nums1, nums2) == 2.5
    
    # Test case 3: Both lists are empty
    nums1 = []
    nums2 = []
    assert sol.findMedianSortedArrays(nums1, nums2) == 0.0

    # Test case 4: One list is empty
    nums1 = [1, 2, 3, 4, 5]
    nums2 = []
    assert sol.findMedianSortedArrays(nums1, nums2) == 3.0
    
    # Test case 5: Duplicates and negatives
    nums1 = [-3, -2, -1, 1, 2, 3]
    nums2 = [0, 0, 0, 0]
    assert sol.findMedianSortedArrays(nums1, nums2) == 0.0
    
pytest.main()
