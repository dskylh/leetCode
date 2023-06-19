from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        s_counter = Counter(s)
        for c in t:
            if c in s_counter.keys() and s_counter[c] != 0:
                s_counter[c] = s_counter[c] - 1
            else:
                return False
        return True


class Solution_2:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

class Solution_3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for cs, ct in zip(s, t):
            count_s[cs] = 1 + count_s.get(cs)
            count_t[ct] = 1 + count_t.get(ct)
        return count_t == count_s
