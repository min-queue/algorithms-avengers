from collections import deque
from typing import List


arr = [6, 2, 6, 5, 1, 2]
arr = [6, 2, 5, 1, 2]


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort(reverse=True)
        print(nums)
        for element in nums[::2]:
            print(element)
        # print(result)

    def sum(self, x, y):
        y += x


s = Solution()
s.arrayPairSum(arr)


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
