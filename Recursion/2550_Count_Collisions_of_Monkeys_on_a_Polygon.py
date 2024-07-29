class Solution:
    def monkeyMove(self, n: int) -> int:
        m = 1000000007
        total = 1
        mult = 2

        while n > 0:
            if n % 2 == 1:
                total = ((total % m) * (mult % m)) % m
                n -= 1
            else:
                mult = ((mult % m) ** 2) % m
                n //= 2
                
        return ((total % m - 2) + m) % m
        