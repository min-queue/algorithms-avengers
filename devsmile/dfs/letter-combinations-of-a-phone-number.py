digits = "23"

dic = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
print(dic)


class Solution:
    def letterCombinations(self, digits: str):
        def dfs(index, p):
            if len(p) == len(digits):
                result.append(p)
                return
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, p + j)

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []
        result = []
        dfs(0, "")
        return result
