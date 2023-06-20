class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        count = {k: 0 for k in set(nums)}
        for n in nums:
            count[n] += 1

        sorted_count = sorted(count.items(), reverse=True, key=lambda x: x[1])
        return [n[0] for n in sorted_count[:k]]


