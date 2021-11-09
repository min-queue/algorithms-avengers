from typing import List

s = ["H","e","l","l","o"]
def solution(s: List[str]) -> List:
    s = [c.lower() for c in s]
    s.reverse()
    return s
solution(s)