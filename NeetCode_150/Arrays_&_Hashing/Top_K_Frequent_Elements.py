from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. Naive solution with HashMap/Dict
        # This solution is O(n^2) in the worst case

        # First create a dict of freq counts for each (unique) element in nums list
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1

        # Initialize list of k freq elements as a set (for O(1) lookups and uniqueness property)
        k_freq_nums = set()
        # Iterate until k_freq_elements has k elements
        while len(k_freq_nums) < k:
            # Find current max freq in freq_dict
            max_freq = 0
            for num in freq_dict:
                max_freq = max(max_freq, freq_dict[num])

            # Go through nums list and add all elements which have max freq to k_freq_nums
            # Note that in this case we can't iterate through freq_dict directly because we need to pop selected elements
            # Typical iterable modification error (size of iterable changes while iterated through it)
            for num in nums:
                if freq_dict[num] == max_freq:
                    k_freq_nums.add(num)
                    freq_dict.pop(num)

        return list(k_freq_nums)

        # There are better solutions like sorting by freq (O(nlogn)) and using a min-heap (O(nlogk))
        # The best solution in O(n) time and space complexity is below:
        # 2. Bucket Sort (Counting Sort is a special case of bucket sort):
        #
        # count_dict = defaultdict(int)
        # # The size of freq array is len(nums) = n because we cannot have a count more than n
        # freq = [[] for i in range(len(nums) + 1)]   # O index empty, fill from 1 to n
        #
        # for num in nums:
        #     count_dict[num] += 1
        #
        # for num, count in count_dict.items():
        #     freq[count].append(num)
        #
        # top_k = []
        # # We want to start with the numbers that occur most frequently, so we go backwards
        # for i in range(len(freq) - 1, 0, -1):
        #     for num in freq[i]:
        #         top_k.append(num)
        #         if len(top_k) == k:
        #             return top_k

        # The most common efficient solution:
        # 3. Min-Heap (O(nlogk)):
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        #
        # heap = []
        # for num in count:
        #     heapq.heappush(heap, (count[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        #
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res