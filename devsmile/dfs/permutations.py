class Solution:
    def permute(self, nums):
        def dfs(left_nums, path):
            if len(left_nums) == 0:
                result.append(path)
            else:
                for num in left_nums:
                    t = left_nums[:]
                    t.remove(num)
                    p = path[:]
                    p.append(num)
                    dfs(t, p)

        result = []

        for n in nums:
            t = nums[:]
            t.remove(n)

            dfs(t, [n])
        return result


input = [1, 2, 3]

print(Solution().permute(input))
