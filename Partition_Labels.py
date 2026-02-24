from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_dict = defaultdict(list)
        ans = []

        for i in range(len(s)):
            s_dict[s[i]].append(i)

        max_ = 0
        sum1 = 0 
        for key in s_dict:
            if s_dict[key][0] <= max_:
                max_ = max(max_, s_dict[key][len(s_dict[key])-1])
            else:
                if len(ans) == 0:
                    ans.append(max_+1)
                    sum1 += max_+1
                else:
                    ans.append(max_+1 - sum1)
                    sum1 +=  max_+1 - sum1    
                max_ = s_dict[key][len(s_dict[key])-1]
        
        if len(ans) == 0:
            ans.append(max_ + 1)
        else:
            ans.append(max_+1 - sum1) 

        return ans 
        
        
