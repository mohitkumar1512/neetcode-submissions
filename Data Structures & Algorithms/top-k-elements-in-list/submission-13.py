class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums: 
            freq[num] += 1
        heap = []
        for num, f in freq.items():
            heapq.heappush(heap, (f, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for f, num in heap]