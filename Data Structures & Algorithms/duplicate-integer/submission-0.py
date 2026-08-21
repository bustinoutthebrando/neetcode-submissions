class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = set()
        for i, j in enumerate(nums):
            if j in prevMap:
                return True
            prevMap.add(j)
        return False
            

        