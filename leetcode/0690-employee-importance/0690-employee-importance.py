"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        my_dict = defaultdict(int)

        for i in range(len(employees)):
            my_dict[employees[i].id] = i

        ans = 0

        visited = set()
        def dfs(node):
            nonlocal ans
            emp = my_dict[node]
            ans += employees[emp].importance
            visited.add(node)

            for negh in employees[emp].subordinates:
                if negh not in visited:
                    dfs(negh)
        
        dfs(id)
        return ans
  