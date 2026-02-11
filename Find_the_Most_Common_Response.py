from collections import Counter
class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        all_responses = []

        for response in responses:
            response_set = set(response)
            all_responses.extend(list(response_set))

        response_count = Counter(all_responses)

        left = 0
        right = 1
        count = 1
        ans = 0
        res = ""

        all_responses.sort()
        while right < len(all_responses):
            if all_responses[left] == all_responses[right]:
                right += 1
                count += 1
                if count > ans:
                    res = all_responses[left]
                    ans = count
            else:
                left = right
                right += 1
                count = 1
        if res:
            return res
        else:
            return all_responses[0]
