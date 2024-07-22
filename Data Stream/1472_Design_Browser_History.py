class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.anchor = 0
        
    def visit(self, url: str) -> None:
        self.anchor += 1
        self.history = self.history[:self.anchor]
        self.history.append(url)

    def back(self, steps: int) -> str:
        if self.anchor >= steps:
            self.anchor -= steps
        else:
            self.anchor = 0
        return self.history[self.anchor]
        
    def forward(self, steps: int) -> str:
        if len(self.history) - self.anchor - 1 >= steps:
            self.anchor += steps
        else:
            self.anchor = len(self.history) - 1
        return self.history[self.anchor]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)