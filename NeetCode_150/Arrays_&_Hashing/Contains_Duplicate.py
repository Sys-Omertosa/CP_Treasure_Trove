class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Simply use a set and compare length
        # Time Complexity O(n) to convert list to set
        if len(set(nums)) != len(nums):
            return True
        return False