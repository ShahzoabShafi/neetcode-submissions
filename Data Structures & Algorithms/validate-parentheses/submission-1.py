from collections import defaultdict


class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open_hashmap = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char in close_to_open_hashmap:
                if stack and stack[-1] == close_to_open_hashmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
