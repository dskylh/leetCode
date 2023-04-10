from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ransomDict = {c: ransomNote.count(c) for c in ransomNote}
        ransomDict = Counter(ransomNote)
        magazineDict = Counter(magazine)



