class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []

        for i in range(len(tasks)):
            tasks[i] = [tasks[i][0], tasks[i][1], i]
        
        tasks.sort()
        t = tasks[0][0]
        # print(tasks)
        i = 0
        while  i < len(tasks) and tasks[i][0] == t:
            heappush(heap, (tasks[i][1], tasks[i][2]))
            i+=1
        
        order = []
        while heap:
            # print(heap,t)
            task = heappop(heap)
            t += task[0]
            order.append(task[1])

            while i < len(tasks) and tasks[i][0] <= t:
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i+=1
            if not heap and i < len(tasks):
                heappush(heap, (tasks[i][1], tasks[i][2]))
                t = tasks[i][0]
                i+=1

        
        return order
