class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            result.append(path)
            for i in range(index, len(nums)):
                p = path[:]
                p.append(nums[i])
                dfs(i + 1, p)

        result = []
        length = len(nums)
        dfs(0, [])
        return result
