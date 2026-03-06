class Node:
    def __init__(self,value):
        self.val = value
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr_br = self.head 

    def visit(self, url: str) -> None:
        new_url = Node(url)
        new_url.prev = self.curr_br
        self.curr_br.next = None
        self.curr_br.next = new_url
        self.curr_br = new_url


    def back(self, steps: int) -> str:
        step = 0
        temp = self.curr_br
        while temp !=self.head and step < steps:
            temp = temp.prev           
            step+=1

        self.curr_br = temp 
        return temp.val

    def forward(self, steps: int) -> str:
        step = 0
        temp = self.curr_br
        while temp.next and step < steps:
            temp = temp.next
            step+=1
        
        self.curr_br = temp
        return temp.val

        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)