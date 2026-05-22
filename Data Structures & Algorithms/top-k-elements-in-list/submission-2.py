class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dick = {}
        for num in nums:
            if num not in dick:
                dick[num] = 1
            else:
                dick[num] += 1
        
        sorted_dicks = sorted(dick, reverse=True, key=lambda x: dick[x])
        return sorted_dicks[:k]