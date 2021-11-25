class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        max_palindrome = ""
        tmp = ""
        if l <= 2:
            return s if s[0] == s[-1] else s[0]

        for index in range(l):
            tmp = self.find_palindrome(index, index, l, s)
            max_palindrome = tmp if len(tmp) > len(max_palindrome) else max_palindrome
            tmp = self.find_palindrome(index, index + 1, l, s)
            max_palindrome = tmp if len(tmp) > len(max_palindrome) else max_palindrome
        return max_palindrome

    def find_palindrome(self, left, right, length, s):
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]
