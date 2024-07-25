class Solution:
    def soupServings(self, n: int) -> float:
        dict_prob = dict()

        def dfs(a: int, b:int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1
            elif b <= 0:
                return 0
            if (a, b) in dict_prob:
                return dict_prob[(a, b)]

            dict_prob[(a, b)] = (dfs(a-100, b) + dfs(a-75, b-25) + dfs(a-50, b-50) + dfs(a-25, b-75)) * 0.25
            return dict_prob[(a, b)]

        return dfs(n, n)