class Solution:
    def isPalindrome(self, s: str) -> bool:
        news=""
        for char in s:
            if char.isalnum():
                news+=char.lower()
        if news==news[::-1]:
            return True
        return False
        