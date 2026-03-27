class Solution(object):
    def letterCombinations(self, digits):
        my_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y","z"],
        }
        ans = []
        
        def backtrack(idx, curr):
            if idx == len(digits):
                ans.append("".join(curr))
                return 
            
            for i in range(len(my_dict[digits[idx]])):
                curr.append(my_dict[digits[idx]][i])
                backtrack(idx+1, curr)
                curr.pop()
        
        backtrack(0,[])
        return ans
