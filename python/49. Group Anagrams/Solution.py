from collections import Counter, defaultdict



class Solution:
    def groupAnagrams(self, strs: list[str]):
        res = {}
        for s in strs:
            sorted_str = tuple(sorted(s))
            res.setdefault(sorted_str, []).append(s)
        return list(res.values())


s = Solution()
res = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(res)
