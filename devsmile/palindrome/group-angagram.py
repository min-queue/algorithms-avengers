import collections
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        [ anagrams["".join(sorted(w))].append(w) for w in strs]
        return anagrams.values()