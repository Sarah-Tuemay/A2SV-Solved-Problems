from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if word1 == word2:
            return True
        word1_count = Counter(word1)
        word2_count = Counter(word2)

        if len(word1_count) == 1 or len(word2_count) == 1:
            return False
        for key in word1_count:
            if key not in word2_count:
                return False
        word1_values = list(word1_count.values())
        word2_values = list(word2_count.values())

        word1_values.sort()
        word2_values.sort()

        return word1_values == word2_values
      
