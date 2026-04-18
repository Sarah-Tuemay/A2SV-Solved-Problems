class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        arr = [(nums[i], i) for i in range(n)]
        
        def merge_sort(start, end):
            if end - start <= 1:
                return arr[start:end]
            
            mid = (start + end) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid, end)
            
            merged = []
            i = j = 0
            right_count = 0
            
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:

                    value, original_index = left[i]
                    result[original_index] += right_count
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    right_count += 1
                    j += 1

            while i < len(left):
                value, original_index = left[i]
                result[original_index] += right_count
                merged.append(left[i])
                i += 1
                
            
            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged
        
        merge_sort(0, n)
        return result