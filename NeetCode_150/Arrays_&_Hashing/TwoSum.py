class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Wickedly difficult for an "easy" problem, at least with a HashMap
        #
        # The first trick is obviously realizing that we instead need to look for diff = target - nums[i]
        # If diff is also in the list nums then we can simply output the current index and the index of diff
        # However doing this with a list alone would be O(n^2) (because we need the indices)
        #
        # The second trick is to maintain a HashMap of {value : index} that keeps updating
        # It calculates diff for each index and checks if it's currently in the HashMap:
        #   1. If not, then simply store the current number as the key and its index as the value
        #   2. If yes, then return a list with the index of diff, and the current index
        #
        # The in operator works in O(1) for HashMaps.
        # A simpler similar solution can be done with lists, but in operator on lists would be O(n^2) inside a for loop which is inefficient

        my_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in my_dict:
                return [my_dict[diff], i]
            my_dict[nums[i]] = i