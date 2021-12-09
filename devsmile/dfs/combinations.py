class Solution:
    def combine(self, n, k):
        def dfs(numbers, result, k):
            if k == 0:
                answer.append(result)
                return
            else:
                for idx, num in enumerate(numbers):
                    result_new = result[:]
                    result_new.append(num)
                    dfs(numbers[idx + 1 :], result_new, k - 1)

        numbers = [n for n in range(1, n + 1)]
        answer = []
        dfs(numbers, [], k)
        return answer
