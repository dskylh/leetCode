class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        p1, p2 = 0, len(numbers) - 1
        while p1 < p2:
            if numbers[p1] + numbers[p2] == target:
                return [p1 + 1, p2 + 1]
            elif numbers[p1] + numbers[p2] > target:
                p2 -= 1
            elif numbers[p1] + numbers[p2] < target:
                p1 += 1


sol = Solution()
sol.twoSum([-3,3,4,90], 0)
