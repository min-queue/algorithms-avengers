from typing import List
from collections import deque


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, result = 0, 1, 0
        blocks = []
        
        while len(height) > right + 1:
            if height[left] <= height[right]:
                # print(blocks)
                # print(height[left],height[right])
                # print("==========")

                result += self.calculate(blocks, min(height[left], height[right]))
                left = right
                right = left + 1
                blocks = []

            elif height[left] > height[right]:
                blocks.append(height[right])
                right += 1
        # print(result)
        # print(blocks)
        # print(height[left], height[right]) 
        right = len(blocks)
        left = 0
        # while left >=right :
        #     if max(blocks) == blocks[left]:
        #         left +=1
                
        #     elif min(blocks) == blocks[right]:
                # right -=1
        # result += self.calculate(block[left:right])
        # left, right = 0
        if len(blocks) != 0 :
            result += self.trap_calculcate(height[::-1],0, 1)
        #     while left < right and max(block) != block[left] and min(block) != block[right]:    
        #         if min(blocks) == height[right]:
        #             result += self.calculate(blocks, max(blocks))
        #         else :
        #             result += self.calculate(blocks, min([height[left], height[right]]))

        return result
    def trap_calculcate(self,height, left, right ):
        blocks=[]
        result = 0
        while len(height) > right + 1:
            if height[left] <= height[right]:
                # print(blocks)
                # print(height[left],height[right])
                # print("==========")

                result += self.calculate(blocks, min(height[left], height[right]))
                left = right
                right = left + 1
                blocks = []

            elif height[left] > height[right]:
                blocks.append(height[right])
                right += 1
            return result
        # print(result)

    def calculate(self, blocks, pillar):
        sum_of_water = 0
        for block in blocks:
            if pillar - block > 0:
                sum_of_water += pillar - block
        return sum_of_water  

# height = [4,2,0,3,2,4,3,4]
height = [4,2,0,3,2,5]
height = [4, 2, 3]
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
# s.trap(height)
# height = [1000,999,998,997,996,996,996,996,996]
print(s.trap(height))
