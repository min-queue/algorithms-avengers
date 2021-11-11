import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphanumeric_str = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        return alphanumeric_str == alphanumeric_str[::-1]


test_case = ["A man, a plan, a canal: Panama", "race a car", " "]
for s in test_case:
    print(Solution().isPalindrome(s))

