class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char) :]
            print(suffix)
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ""))
        return ""


a = "cbacdcbc"
print(a[1:])
