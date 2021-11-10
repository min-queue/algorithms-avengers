from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = defaultdict(int)
        for i, num in enumerate(nums) :
            t[num] = i
        print(t)
        for i, num in enumerate(nums):
            sub_number = target - num
            if t.get(sub_number) is not None and i != t.get(sub_number):
                return [i, t.get(sub_number)]