import re
from collections import Counter
from typing import List


def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = re.sub(r"[^\w]", " ", paragraph).lower().split()
    filltered_words = [w for w in words if w not in banned]
    return Counter(filltered_words).most_common(1)[0][0]
