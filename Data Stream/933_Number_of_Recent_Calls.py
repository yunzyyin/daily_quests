class RecentCounter:

    def __init__(self):
        self.time_of_calls = list()
        
    def ping(self, t: int) -> int:
        recent_calls = 1
        for i in self.time_of_calls:
            if i >= t-3000:
                recent_calls += 1
        self.time_of_calls.append(t)
        return recent_calls
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)