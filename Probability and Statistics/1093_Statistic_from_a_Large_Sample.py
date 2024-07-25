class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        min = 255
        max = 0
        max_repeat_times = 0
        max_repeat_num = None
        sum_elements = 0
        count_elements = 0
        count_extract = {}

        for idx, val in enumerate(count):
            if val != 0:
                if idx < min:
                    min = idx
                if idx > max:
                    max = idx
                if val > max_repeat_times:
                    max_repeat_times = val
                    max_repeat_num = idx
                sum_elements += idx*val
                count_elements += val
                count_extract[idx] = val

        def find(index: int) -> int:
            total = 0
            for k, v in count_extract.items():
                total += v
                if index <= total:
                    return k
        
        if count_elements % 2 != 0:  # odd number
            median = find(count_elements//2+1)
        else:  # even number
            median = (find(count_elements/2) + find(count_elements/2+1))/2

        return min, max, sum_elements/count_elements, median, max_repeat_num
