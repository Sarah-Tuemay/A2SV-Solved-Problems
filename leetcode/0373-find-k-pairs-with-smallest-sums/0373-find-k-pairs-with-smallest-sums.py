from heapq import heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []

        heap = [(nums1[0] + nums2[0], 0, 0)]
        visited = {(0, 0)}
        res = []

        while heap and len(res) < k:
            sum1, i, j = heappop(heap)
            res.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

        return res