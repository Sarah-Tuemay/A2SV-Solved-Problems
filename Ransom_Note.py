from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for key in ransomNote_count:
            if key not in magazine_count:
                return False
            if ransomNote_count[key] > magazine_count[key]:
                return False
        return True 
