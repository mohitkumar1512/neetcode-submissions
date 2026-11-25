class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums: 
            freq[n] += 1
        
        heap = []
        for key, v in freq.items():
            heapq.heappush(heap, (v, key))
            if len(heap) > k: 
                heapq.heappop(heap)
        return [item[1] for item in heap]