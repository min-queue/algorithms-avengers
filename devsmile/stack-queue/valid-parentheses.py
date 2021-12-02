class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        my_dict = {")": "(", "]": "[", "}": "{"}
        if len(s) <= 1:
            return False

        for e in s:
            if e in ["(", "{", "["]:
                my_stack.append(e)
            elif e in [")", "}", "]"] and len(my_stack) > 0:
                pp = my_stack.pop()
                if pp != my_dict[e]:
                    return False
            else:
                return False

        if len(my_stack) > 0:
            return False

        return True
