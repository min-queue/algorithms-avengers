 class Solution:
        def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target, candidates, nums):
            if target == sum(nums):
                result.append(nums)
                return
            elif target < sum(nums):
                return
            else :
                for idx, n in enumerate(candidates):

                    new_nums = nums[:]
                    new_nums.append(n)
                    dfs(target, candidates[idx:], new_nums)
        result = []

        dfs(target, candidates, [])
        return result