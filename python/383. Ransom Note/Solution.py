from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDict = Counter(ransomNote)
        magazineDict = Counter(magazine)
        for letter in ransomDict.keys():
            if letter in magazineDict.keys() and ransomDict.get(letter) <= magazineDict.get(letter):
                magazineDict[letter] -= ransomDict.get(letter)
                ransomDict[letter] = 0

        return sum(ransomDict.values()) == 0

