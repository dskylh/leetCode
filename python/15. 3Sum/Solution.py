class Solution:
    def threeSum(self, nums: list[int]):
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i != 0 and n == nums[i - 1]:
                continue
            p1, p2 = i + 1, len(nums) - 1

            while p1 < p2:
                s = n + nums[p1] + nums[p2]
                if s < 0:
                    p1 += 1
                elif s > 0:
                    p2 -= 1
                else:
                    res.append([n, nums[p1], nums[p2]])
                    p1 += 1
                    while nums[p1] == nums[p1 - 1] and p1 < p2:
                        p1 += 1
        return res


sol = Solution()
sol.threeSum([-1, 0, 1, 2, -1, -4])
