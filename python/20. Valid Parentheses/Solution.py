class Solution:
    def isValid(self, s: str) -> bool:
        p = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in p.keys():
                if stack and stack[-1] == p[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

sol = Solution()
sol.isValid("({{()}})")

