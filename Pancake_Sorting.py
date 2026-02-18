class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        ans = []
        i = 0
        max_index = len(arr)-1
        while i < len(arr):
            max_ele = max(arr[:max_index + 1])
            idx = arr.index(max_ele)
            if idx != max_index:
                arr[:idx + 1] = arr[idx::-1]
                ans.append(idx+1)
                arr[:max_index + 1] = arr[max_index::-1]
                ans.append(max_index+1)
            max_index -= 1
            i+=1

        return ans
