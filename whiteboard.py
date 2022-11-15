# 1Check if Number and its double exists
# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
# More formally check if there exists two indices i and j such that :
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
# Example 2:
# Input: arr = [7,1,14,11]
# Output: true
# Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
# Example 3:
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: In this case does not exist N and M, such that N = 2 * M.


def find_doubles(nums):
    for i in range(len(nums)):
        for j in (nums[:i]+nums[i+1:]):
            if nums[i] * 2 == j:
                return True
    return False
    # 2n^2


# print(find_doubles([7, 1, 14, 11]))


def find_doubles_set(nums):
    nums_set = set(nums)
    for num in nums_set:
        if num * 2 in nums_set or num / 2 in nums_set:
            return True
    return False
    # 2n


# print(find_doubles_set([7, 1, 14, 11]))


def one_liner(nums):
    return True if [num for num in nums if num / 2 in nums or num * 2 in nums] else False
    # 2n


print(one_liner([7, 1, 13, 11]))
print(one_liner([7, 1, 14, 11]))
