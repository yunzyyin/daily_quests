import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        star_to_remove = []
        previous_star_pos = None
        for pos in range(len(p)):
            if p[pos] == "*":
                if previous_star_pos and previous_star_pos == pos-1:
                    star_to_remove.append(pos)
                previous_star_pos = pos
        star_to_remove.reverse()
        for pos in star_to_remove:
            p = p[:pos] + p[pos+1:]
        p = p + "$"
        return bool(re.match(p,s))
        