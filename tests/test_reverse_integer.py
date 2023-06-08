import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from reverse_integer import Solution

# Create an instance of the Solution class
solution = Solution()

def test_reverse_positive():
    assert solution.reverse(123) == 321

def test_reverse_negative():
    assert solution.reverse(-123) == -321

def test_reverse_zero():
    assert solution.reverse(0) == 0

def test_reverse_large_number():
    assert solution.reverse(1534236469) == 0

def test_reverse_boundary():
    assert solution.reverse(2147483648) == 0

def test_reverse_boundary_negative():
    assert solution.reverse(-2147483649) == 0

# Run the tests
pytest.main()
