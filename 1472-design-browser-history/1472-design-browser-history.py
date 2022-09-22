
class Node:
    def __init__(self,page):
        self.page=page
        self.next=None
        self.prev=None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage=Node(homepage)
        
    def visit(self, url: str) -> None:
        newpage=Node(url)
        self.homepage.next=newpage
        newpage.prev=self.homepage
        self.homepage=self.homepage.next
        
    def back(self, steps: int) -> str:
        print(self.homepage.page)
        for i in range(steps):
            if self.homepage.prev is None:
                return self.homepage.page
            else:
                self.homepage=self.homepage.prev
        return self.homepage.page

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.homepage.next is None:
                return self.homepage.page
            else:
                self.homepage=self.homepage.next
        return self.homepage.page



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)