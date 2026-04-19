class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            return 0
            
        min_val = min(nums)
        max_val = max(nums)

        if min_val == max_val:
            return 0

        bucket_size = max(1, (max_val - min_val) // (N - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        buckets = [{"min": None, "max": None} for _ in range(bucket_count)]

        for num in nums:
            idx = (num - min_val) // bucket_size

            if num == max_val:
                idx = bucket_count - 1
                
            if buckets[idx]["min"] is None:
                buckets[idx]["min"] = num
                buckets[idx]["max"] = num
            else:
                buckets[idx]["min"] = min(num, buckets[idx]["min"])
                buckets[idx]["max"] = max(num, buckets[idx]["max"])

        max_gap = 0
        prev_max = min_val
        
        for bucket in buckets:
            if bucket["min"] is None:
                continue
                
            max_gap = max(bucket["min"] - prev_max, max_gap)
            prev_max = bucket["max"]
            
        return max_gap