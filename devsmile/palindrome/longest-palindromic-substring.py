class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        max_palindrome = ""
        tmp = ""
        if l <=2: return s if s[0]==s[-1] else s[0]

        for index in range(l):
            if l % 2 == 0:
                tmp = self.find_palindrome(index, index + 1, l, s)
            else:
                tmp = self.find_palindrome(index, index, l, s)
            print(tmp)
            max_palindrome = tmp if len(tmp) > len(max_palindrome) else max_palindrome
        return max_palindrome

    def find_palindrome(self, left, right, length, s):
        palindrome_word = ""
        while left >= 0 and right < length :
            if (s[left]!= s[right]):
                return palindrome_word
            else:
                palindrome_word = s[left:right+1]
            left -=1
            right +=1
        return palindrome_word


s = Solution()
print('answer is ',s.longestPalindrome("abb"))




class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]