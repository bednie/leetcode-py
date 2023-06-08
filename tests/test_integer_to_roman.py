import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from integer_to_roman import Solution

def test_intToRoman():
    solution = Solution()

    # positive test cases
    assert solution.intToRoman(1) == 'I'
    assert solution.intToRoman(4) == 'IV'
    assert solution.intToRoman(9) == 'IX'
    assert solution.intToRoman(58) == 'LVIII'
    assert solution.intToRoman(1994) == 'MCMXCIV'
    assert solution.intToRoman(3999) == 'MMMCMXCIX'
    
    # negative test cases
    with pytest.raises(Exception):
        assert solution.intToRoman(0) # should raise an exception as the value is out of range
        assert solution.intToRoman(4000) # should raise an exception as the value is out of range

pytest.main()