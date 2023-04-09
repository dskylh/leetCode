class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        temp = 0
        for num in nums:
            temp = num + temp
            result.append(temp)
        return result
