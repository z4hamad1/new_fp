"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    cur_sum = 0
    start = 0

    for i in range(len(nums)):
        cur_sum += nums[i]

        if i >= k:
            cur_sum -= nums[start]
            start += 1

        max_sum = max(max_sum, cur_sum)

    return max_sum


if __name__ == "__main__":
    print(find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3))
