class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for ch in s:
            if ch in mapping.values():   # opening brackets
                stack.append(ch)
            else:  # closing brackets
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
        
        return len(stack) == 0
                             
        