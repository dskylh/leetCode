from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]):
        prefix = 1
        postfix = 1
        answer = [1] * len(nums)
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
