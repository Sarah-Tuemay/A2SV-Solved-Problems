class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        new_arr = []
        cnt = 0
        for i in range(len(nums1)):
            new_arr.append(nums1[i]-nums2[i])
        

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr)//2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)
        
        def merge(left, right):
            nonlocal cnt
            result = []
            i = j = 0

            for t in range(len(right)):
                cnt += (bisect_right(left, right[t]+diff))

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            
            result.extend(left[i:])
            result.extend(right[j:])

            return result
        
        merge_sort(new_arr)
        return cnt

