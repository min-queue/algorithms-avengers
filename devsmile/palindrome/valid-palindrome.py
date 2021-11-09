import re

a = "A man, a plan, a canal: Panama"


def solution(s: str) -> bool:
    s = re.sub("[^a-zA-Z0-9]", "", s).lower()
    return s[::-1] == s


solution(a)
