from typing import List


nums = [-1, 0, 1, 2, -1, -4]
nums = [0, 0, 0, 0, 0, 0]
nums = [-2, 0, 1, 1, 2]
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         length = len(nums)
#         result = []
#         for i, pivot_num in enumerate(nums):
#             if i + 2 > length: break
#             left, right = i + 1, length - 1
#             sum_numbers = self.find_zero_sum(left, right, pivot_num, nums)
#             if sum_numbers is not None and sum_numbers not in result:
#                 result.extend(sum_numbers)
#         return result

#     def find_zero_sum(self, left, right, pivot_nums, nums):
#         result
#         while(left < right ):
#             if pivot_nums + nums[left] + nums[right] > 0:
#                 right -=1
#             elif pivot_nums + nums[left] + nums[right] < 0:
#                 left +=1
#             elif pivot_nums + nums[left] + nums[right] == 0:
#                 return  [ pivot_nums, nums[left], nums[right] ]
#         return None


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        result = []
        for i, pivot_num in enumerate(nums):
            if i + 2 > length:
                break
            left, right = i + 1, length - 1
            sum_numbers = self.find_zero_sum(left, right, pivot_num, nums, result)
            if sum_numbers is not None and sum_numbers not in result:
                result = sum_numbers
        return result

    def find_zero_sum(self, left, right, pivot_nums, nums, result):
        while left < right:
            print(pivot_nums, nums[left], nums[right])
            if pivot_nums + nums[left] + nums[right] > 0:
                right -= 1
            elif pivot_nums + nums[left] + nums[right] < 0:
                left += 1
            elif pivot_nums + nums[left] + nums[right] == 0:
                if [pivot_nums, nums[left], nums[right]] not in result:
                    result.append([pivot_nums, nums[left], nums[right]])
                left += 1
                right -= 1

        return result


s = Solution()
print(s.threeSum(nums))
# s.threeSum(nums)
