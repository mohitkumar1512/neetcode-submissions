class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        largest = -1
        for num in arr: 
            freq[num] += 1
        for n, c in freq.items():
            if n == c:
                largest = max(largest, n)
        return largest