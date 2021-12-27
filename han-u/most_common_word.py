import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub("[!?',;.]", '', paragraph).lower().split(" ")
        count = {}
        for word in words:
            if word not in banned:
                count.setdefault(word, 0)
                count[word] += 1
        sorted_words = [k for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)]
        return sorted_words[0]
