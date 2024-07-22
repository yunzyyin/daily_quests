class StockSpanner:

    def __init__(self):
        self.price_history = list()

    def next(self, price: int) -> int:
        span = 1
        for pre_price in self.price_history:
            if pre_price <= price:
                span += 1
            else:
                break
        self.price_history.insert(0, price)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)