class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        best_unfairness = float('inf')
        comb = [0] * k

        def backtrack(idx):
            nonlocal best_unfairness 
            
            if idx == len(cookies):
                current_unfairness = max(comb)  
                best_unfairness = min(best_unfairness, current_unfairness)
                return
        
            for i in range(k):
                comb[i] += cookies[idx]
                if comb[i] < best_unfairness:
                    backtrack(idx + 1)
                    
                comb[i] -= cookies[idx]
                
        backtrack(0)
        return best_unfairness