class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre_sum = [0] * len(nums)

        for request in requests:
            pre_sum[request[0]] += 1
            if request[1] != len(nums)-1:
                pre_sum[request[1]+1] -= 1
        
        sum1 = 0

        for i in range(len(pre_sum)):
            sum1 += pre_sum[i]
            pre_sum[i] = sum1
        
        list1 = []

        for index, num in enumerate(pre_sum):
            list1.append([num, index])
        
        list1.sort(reverse= True)

        nums.sort(reverse=True)

        new_nums = [0] * len(nums)
        ptr = 0

        for li in list1:
            new_nums[li[1]] = nums[ptr]
            ptr+=1

        summ = 0

        for i in range(len(new_nums)):
            summ += new_nums[i]
            new_nums[i] = summ
        
        ans = 0
        for req in requests:
            ans += new_nums[req[1]]
            if req[0] != 0:
                ans -= new_nums[req[0]-1]
        
        return ans % (10 ** 9 + 7)
