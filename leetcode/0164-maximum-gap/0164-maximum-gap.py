class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        N = len(nums)
\
        bucket_val = [{"min": None, "max": None} for _ in range(N)]

        min_ = min(nums)
        range_ = max(nums) - min_
        if range_ == 0:
            return 0
        for num in nums:
            idx = int(N*(num-min_)//range_)

            if idx == N:
                idx-=1

            if bucket_val[idx]["min"] == None:
                bucket_val[idx]["min"] = num
                bucket_val[idx]["max"] = num
            else:
                bucket_val[idx]["min"] = min(bucket_val[idx]["min"], num)
                bucket_val[idx]["max"] = max(bucket_val[idx]["max"], num)
        
        prev_max = min_
        diff = 0

        for bucket in bucket_val:

            if bucket['min'] == None:
                continue
            diff = max(bucket['min']-prev_max, diff)
            prev_max = bucket['max']
        
        return diff

        # print(bucket_val)

