from typing import Counter


class Solution:
    def containsDuplicate(self, nums: list[int]):
        return True if len(set(nums)) < len(nums) else False
    # return len(set(nums)) != len(nums)


class Solution_2:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False
