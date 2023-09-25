class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        rain = 0
        p1 = 0
        p2 = len(height) - 1
        maxp1 = height[p1]
        maxp2 = height[p2]
        while p1 < p2:
            if maxp1 < maxp2:
                p1 += 1
                maxp1 = max(maxp1, height[p1])
                rain += maxp1 - height[p1]
            else:
                p2 -= 1
                maxp2 = max(maxp2, height[p2])
                rain += maxp2 - height[p2]
        return rain
