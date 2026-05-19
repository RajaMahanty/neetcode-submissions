class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = {}
        for i in nums:
            if i not in numSet:
                numSet[i] = 1
            else:
                numSet[i] += 1
            if numSet[i] > 1:
                return True
        return False