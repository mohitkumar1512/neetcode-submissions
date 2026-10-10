class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = defaultdict(int)
        for num in nums:
            topK[num] += 1
        sorted_d = dict(sorted(topK.items(), key=lambda x: x[1], reverse=True))
        return list(sorted_d.keys())[:k]
        
