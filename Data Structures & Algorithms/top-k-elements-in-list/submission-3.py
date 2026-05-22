from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums)
        return [x for x, _ in n.most_common(k)]
        # dick = {}
        # for num in nums:
        #     if num not in dick:
        #         dick[num] = 1
        #     else:
        #         dick[num] += 1
        
        # sorted_dicks = sorted(dick, reverse=True, key=lambda x: dick[x])
        # return sorted_dicks[:k]