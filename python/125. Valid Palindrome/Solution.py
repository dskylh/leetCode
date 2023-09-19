class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.alphNum(s.lower().strip())
        pointer_one = 0
        pointer_two = len(s) - 1
        while pointer_one < pointer_two:
            if s[pointer_one] != s[pointer_two]:
                return False
            pointer_one += 1
            pointer_two -= 1
        return True
    
    def alphNum(self, s: str) -> str:
        res = ""
        for c in s:
            if c.isalnum():
                res += c
            else:
                continue
        return res
                
        
sol = Solution()
sol.isPalindrome("race a car")