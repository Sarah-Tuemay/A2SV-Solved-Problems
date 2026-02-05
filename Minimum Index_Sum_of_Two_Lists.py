import sys
class Solution(object):
    def findRestaurant(self, list1, list2):
        list1_dict = {}
        list2_dict = {}
        ans = []

        for index, item in enumerate(list1):
            list1_dict[item] = index
        for index, item in enumerate(list2):
            list2_dict[item] = index
        
        min_index = sys.maxsize
        for key in list1_dict:
            if key in list2_dict:
                if list1_dict[key] + list2_dict[key] < min_index:
                    min_index = list1_dict[key] + list2_dict[key]
        for key in list1_dict:
            if key in list2_dict:
                if list1_dict[key] + list2_dict[key] == min_index:
                    ans.append(key)

        return ans
