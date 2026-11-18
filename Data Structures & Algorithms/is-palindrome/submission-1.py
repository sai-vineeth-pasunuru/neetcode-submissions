class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(char for char in s if char.isalnum())
        if t.lower() == t[::-1].lower():
            return(True)
        return(False)