import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from valid_parentheses import Solution

@pytest.fixture
def solution():
    return Solution()

def test_valid_parentheses(solution):
    assert solution.isValid("") == False
    assert solution.isValid("()") == True
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("{[]}") == True
    assert solution.isValid("(]") == False
    assert solution.isValid("([)]") == False
    assert solution.isValid("[") == False
    assert solution.isValid("}") == False
    assert solution.isValid("[(])") == False
    assert solution.isValid("({{[()}}]") == False

pytest.main()