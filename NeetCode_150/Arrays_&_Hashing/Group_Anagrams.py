from collections import defaultdict

class Solution:
     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Actually devious (if all medium problems are like this we are cooked fr fr)
        # The optimal O(m*n) solution is as follows, using arrays and a HashMap
        #
        # Firstly we use a defaultDict instead of a normal dict
        # so that we don't have to deal with KeyError shenanigans
        # (i.e. key doesn't exist but we're trying to append to a list corresponding to the non-existent key)
        #
        # We iterate through the list of strings and initialize an array count for each string
        # The idea for count is similar to one of the solutions for Value_Anagram
        # i.e. since there are 26 possible letters (a-z), we use a 26-size array
        # with indices -> normalized letter number, and value -> frequency of letter in string
        #
        # We then iterate through the current string and calculate the count array for it
        # Then we simply store into the dict with key -> array and value -> list of string that match the array
        # This works because HashMap keys are akin to sets. They only keep unique values
        # If a key "reoccurs" in this case, the new string is just appended to the corresponding list. No extra key is added
        # Note that to use as a key count must be converted to a tuple first because Python doesn't accept mutable datatypes as dict keys
        #
        # Very intuitive solution that shows how flexible and varied the use of HashMaps can be

        my_dict = defaultdict(list)     # Stores freq array : [str1, str2, ...]
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord('a')] += 1
            my_dict[tuple(count)].append(str)

        return list(my_dict.values())

        # Alt: Using sorting (Time Complexity: O(m * nlogn)
        # This solution also uses a HashMap with the same idea that repeated occurrences of the key mean appending to a list
        # Simply sort each string in the list first
        # The sorted version is the key, while the corresponding list of original strings is the value
        # Simpler and takes less space, but is more time-inefficient
        #
        # res = defaultdict(list)
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)
        # return list(res.values())