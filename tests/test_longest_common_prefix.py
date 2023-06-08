import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from longest_common_prefix import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.fixture(params=[
    (['flower', 'flow', 'flight'], 'fl'),
    (['dog', 'racecar', 'car'], ''),
    (['intensive', 'interior', 'in'], 'in'),
    (['a'], 'a'),
])
def prefix_cases(request):
    return request.param

def test_longest_common_prefix(solution, prefix_cases):
    strs, expected = prefix_cases
    result = solution.longestCommonPrefix(strs)
    assert result == expected

pytest.main()