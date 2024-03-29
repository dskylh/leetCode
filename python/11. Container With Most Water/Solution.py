class Solution:
    def maxArea(self, height: list[int]) -> int:
        p1, p2 = 0, len(height) - 1
        m = 0
        while p1 < p2:
            m = max(m, min(height[p1], height[p2]) * (p2 - p1))
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
        return m


sol = Solution()
sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
