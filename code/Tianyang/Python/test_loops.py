import pytest
# def double_numbers(nums):
#     new_list = []
#     for num in nums:
#         new_list.append(num*2)
#     return new_list

# def test_double_numbers():
#     assert double_numbers([1, 2, 3]) == [2, 4, 6]


def stars(n):
    result = []
    result.append('*'*n)
    return (''.join(result))

def test_stars():
    assert stars(1) == '*'
    assert stars(2) == '**'
    assert stars(3) == '***'
    assert stars(4) == '****'