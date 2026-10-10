class TimeMap:

    def __init__(self):
        self.freq = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.freq[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.freq[key]

        l = 0
        r = len(values) - 1
        ret = ""  

        while l <= r: 
            m = (l + r) // 2
            if values[m][1] <= timestamp: 
                ret = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return ret
            
