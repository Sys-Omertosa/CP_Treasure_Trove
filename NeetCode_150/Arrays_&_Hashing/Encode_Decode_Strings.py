class Solution:

    # Fairly easy for a medium problem
    # Simply have an instance variable str_lengths that is a list of the lengths of the strings in strs
    # To encode, simply use .join() to concatenate strings in O(n) time in one go
    # To decode, use the str_lengths list to determine where each string starts and ends in the encoded string

    def __init__(self):
        self.str_lengths = []

    def encode(self, strs: list[str]) -> str:
        for string in strs:
            self.str_lengths.append(len(string))
        return "".join(strs)

    def decode(self, s: str) -> list[str]:
        str_list = []
        start_index = 0
        for length in self.str_lengths:
            str_list.append(s[start_index:length+start_index])
            start_index += length
        return str_list

    # Another intuitive solution in O(m) time and O(m+n) space
    # where m is the sum of lengths of all the strings and n is the number of strings:
    #
    # def encode(self, strs: List[str]) -> str:
    #         res = ""
    #         for s in strs:
    #             # Avoid concatenation here as string concatenation in Python is O(n^2). Use .join() instead
    #             res += str(len(s)) + "#" + s
    #         return res
    #
    #     def decode(self, s: str) -> List[str]:
    #         res = []
    #         i = 0
    #
    #         while i < len(s):
    #             j = i
    #             while s[j] != '#':
    #                 j += 1
    #             length = int(s[i:j])
    #             i = j + 1
    #             j = i + length
    #             res.append(s[i:j])
    #             i = j
    #
    #         return res

solution1 = Solution()
print(solution1.decode(solution1.encode(["we","say",":","yes"])))