class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # topK = defaultdict(int)
        # for num in nums:
        #     topK[num] += 1
        # sorted_d = dict(sorted(topK.items(), key=lambda x: x[1], reverse=True))
        # return list(sorted_d.keys())[:k]
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, freq in count.items():
            buckets[freq].append(val)
        print(buckets)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            res.extend(buckets[i])
            if len(res) >= k:
                return res[:k]
