from typing import List
from collections import deque

# 투포인터 문제
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
             return 0
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            if left_max <= right_max:
                volume  += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -=1
        return volume
    # def trap(self, height: List[int]) -> int:
    #     left, right, result = 0, 1, 0
    #     blocks = []
        
    #     while len(height) > right + 1:
    #         if height[left] <= height[right]:
    #             result += self.calculate(blocks, min(height[left], height[right]))
    #             left = right
    #             right = left + 1
    #             blocks = []

    #         elif height[left] > height[right]:
    #             blocks.append(height[right])
    #             right += 1

    #     right = len(blocks)
    #     left = 0
    #     if len(blocks) != 0 :
    #         result += self.trap_calculcate(height[::-1],0, 1)

    #     return result
    # def trap_calculcate(self,height, left, right ):
    #     blocks=[]
    #     result = 0
    #     while len(height) > right + 1:
    #         if height[left] <= height[right]:
    #             result += self.calculate(blocks, min(height[left], height[right]))
    #             print(blocks)
    #             left = right
    #             right = left + 1
    #             blocks = []

    #         elif height[left] > height[right]:
    #             blocks.append(height[right])
    #             right += 1
    #         return result
    #     # print(result)

    # def calculate(self, blocks, pillar):
    #     sum_of_water = 0
    #     for block in blocks:
    #         if pillar - block > 0:
    #             sum_of_water += pillar - block
    #     return sum_of_water  

# height = [4,2,0,3,2,4,3,4]
height = [4,2,0,3,2,5]
# height = [4, 2, 3]
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
# s.trap(height)
# height = [1000,999,998,997,996,996,996,996,996]
print(s.trap(height))
