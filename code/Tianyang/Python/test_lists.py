import pytest
#1
# def even_even(nums):
#     nums_list = []
#     i = 0
#     for num in nums:
#         if num % 2 == 0:
#             i += 1
#         else:
#             i = i
#     if i % 2 == 0:
#         return True
#     else:
#         return False

# def test_even_even():
#     assert even_even([5, 6, 2]) == True
#     assert even_even([5, 5, 2]) == False


#2
# def reverse(nums):
#     nums_list = []
#     return nums_list.reverse

# def test_reverse():
#     assert reverse([1, 2, 3]) == [3, 2, 1]

#3
# def common_elements(nums1, nums2):
#     common_list = []
#     for a in nums1:
#         for b in nums2:
#             if a == b:
#                 common_list.append(a)
#     return common_list

# # def test_common_elements():
# #     assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]

#4
def combine(nums1, nums2):
    com_list = []
    for a in range(len(nums1)):
         com_list.append(nums1[a])
         com_list.append(nums2[a])
    return com_list
        
# def test_combine():
#     assert combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]
print(combine(['a', 'b', 'c'], [1, 2, 3]))