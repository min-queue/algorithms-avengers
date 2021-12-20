from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_arr = []
        letter_arr = []
        for log in logs:
            if log.split(" ")[1].isdigit():
                digit_arr.append(log)
            else:
                letter_arr.append(log)
        letter_arr = sorted(letter_arr, key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))
        return letter_arr + digit_arr
