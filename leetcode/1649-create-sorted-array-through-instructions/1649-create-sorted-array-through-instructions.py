class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        N=len(instructions)
        less=[0] * N
        great=[0] * N
        instructions=[(ins, i) for i,ins in enumerate(instructions)]
        cost = [0]
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            half = len(arr)//2

            right = merge_sort(arr[half:])
            left = merge_sort(arr[:half])

            return merge(left, right)
        
        def merge(left, right):
            # print(left,right)
            # print(right)
            res = []
            for num, i in right:
                idx = bisect_left(left,(num, float('-inf')))
                idx2 = bisect_right(left, (num, float('inf')))
                less[i]+=idx
                great[i]+=len(left)-idx2
            i=j=0

            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    res.append(left[i])
                    i+=1
                
                else:
                    res.append(right[j])
                    j+=1
            # print(less)
            # print(great)
            
            res.extend(left[i:])
            res.extend(right[j:])

            return res
        
        merge_sort(instructions)

        cost = 0

        # print(less)
        # print(great)
        for i in range(len(less)):
            cost += min(less[i], great[i])
        
        return cost%(pow(10,9)+7)

