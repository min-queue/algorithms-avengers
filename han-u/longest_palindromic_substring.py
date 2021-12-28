class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = []
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if s[i:j+1] == s[i:j+1][::-1]:
                    palindrome.append(s[i:j+1])
        return max(palindrome, key=len)
