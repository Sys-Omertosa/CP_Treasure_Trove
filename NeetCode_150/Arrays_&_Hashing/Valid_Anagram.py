class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # The simplest solution, but unfortunately takes O(nlogn + mlogm) time complexity
        # where n = len(s) and m = len(t)
        # Simply sort both strings by ASCII values and compare:
        return sorted(s) == sorted(t)

        # Alt 1: Using HashMaps of frequencies:
            # Maintain a hashmap for each string
            # where a key is the letter and value is the freq of the letter in the string
            # Then simply compare the two hashmaps
            # You can reach this solution by realizing that we are concerned with two things this time:
            #   1. If the two strings have the same characters
            #   2. If the number (freq) of those same characters are equal

            # if len(s) != len(t):
            #     return False
            #
            # countS, countT = {}, {}
            #
            # for i in range(len(s)):
            #     countS[s[i]] = 1 + countS.get(s[i], 0)
            #     countT[t[i]] = 1 + countT.get(t[i], 0)
            # return countS == countT

            # The above code can actually be written in one line using a specialized Python container, Counter()
            # from collections import Counter
            #
            # counter = Counter(iterable)
            # return Counter(s) == Counter(t)

        # Alt 2: Hash Table:
            # Keep a 26-size array count (for all possible letters)
            # where index is the ASCII of the letter, normalized by ASCII of 'a'
            # and value is the 'count' of the letter
            # Iterate through the length of a string (after checking if length is same):
            #   1. Increment value at index of letter if it's in s
            #   2. Decrement value at index of letter if it's in t
            # If anagram, all values in the count array should be 0

            # if len(s) != len(t):
            #     return False
            #
            # count = [0] * 26
            # for i in range(len(s)):
            #     count[ord(s[i]) - ord('a')] += 1
            #     count[ord(t[i]) - ord('a')] -= 1
            #
            # for val in count:
            #     if val != 0:
            #         return False
            # return True