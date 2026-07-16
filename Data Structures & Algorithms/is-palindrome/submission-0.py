class Solution:
    def isAlphaNumeric(self, c: str) -> bool:
        return ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1        
        while l <= r:
            if not self.isAlphaNumeric(s[l]):
                l += 1
                continue
            
            if not self.isAlphaNumeric(s[r]):
                r -= 1
                continue
            
            if s[l] != s[r]:
                return False
            else:
                l, r = l+1, r-1
        return True

        