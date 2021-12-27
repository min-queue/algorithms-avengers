from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for str in strs:
            key = "".join(sorted(str.lower()))
            anagram.setdefault(key, []).append(str)
        return anagram.values()
