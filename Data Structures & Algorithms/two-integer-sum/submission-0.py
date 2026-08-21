class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        emptyList = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in emptyList:
                return[emptyList[diff], i]
            emptyList[j] = i
        return
        

