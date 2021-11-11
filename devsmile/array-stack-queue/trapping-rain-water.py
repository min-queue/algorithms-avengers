from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = max(height)
        length = len(height)
        result = 0
        for i, h in enumerate(height):
            max_pillar=0
            if h == max_height:
                if i!=length-1 and max(height[i+1:length]) == max_height:
                    print(self.calculate(height[i+1:length], h))
            elif max(height[i+1:length]) >= max_pillar:
                print(max(height[i+1:length]))


    def calculate(self, blocks, pillar):
        sum_of_water = 0
        for block in blocks:
            sum_of_water += pillar-block
        return sum_of_water

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 3]
s = Solution()
s.trap(height)
