class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for l in logs:
            if l.split()[1].isdigit():
                digits.append(l)
            else:
                letters.append(l)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits