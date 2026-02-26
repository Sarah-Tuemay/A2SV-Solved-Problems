from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = defaultdict(int)
        # window_size = 0
        left = 0
        max_ = 0

        for right in range(len(s)):
            # window_size += 1
            my_dict[s[right]] += 1

            while (right-left+1) - max(my_dict.values()) > k:
                my_dict[s[left]]-=1
                # window_size -= 1 
                left += 1
            
            max_ = max(max_, right-left+1)

        return max_        
