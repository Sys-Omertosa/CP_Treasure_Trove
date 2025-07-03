class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Fairly easy problem to solve with division operator
        # You can simply take the product of all elements in the array
        # and for each position, divide the num by the total product
        # You would have to look out for the following edge cases:
        #   1. There are multiple zeroes    -> return output with all elements = 0
        #   2. There is one zero            -> return output with the product of one position without zero, and all other elements = 0
        #   3. There are no zeroes          -> simply divide total product by num in current position

        # Division based solution:
        #
        # output = [0] * len(nums)
        # prod, zero_count = 1, 0
        # for index, num in enumerate(nums):
        #     if num == 0:
        #         zero_count += 1
        #         if zero_count > 1:
        #             return output
        #         zero_index = index
        #     else:
        #         prod *= num
        #
        # if zero_count > 0:
        #     output[zero_index] = prod
        # else:
        #     for index, num in enumerate(nums):
        #         output[index] = prod // num
        # return output

        # However the constraint in this problem requires and O(n) solution WITHOUT using division
        # To do this we require a prefix-suffix approach
        # We can use separate prefix and suffix arrays, but the most optimal way is to use the output array itself
        # This approach requires the understanding that, for a num in nums, the product of all nums except num requires:
        #   1. The product of all nums BEFORE it | to the LEFT of it | the prefix
        #   2. The product of all nums AFTER it | to the RIGHT of it | the suffix
        # The product of the prefix and suffix gives the total product of the nums excluding num
        # E.g: [1, 2, 3, 4, 5]. For num = 3, we want 1 x 2 x 4 x 5
        # [1, 2 | 3 | 4 , 5]
        #   1. 1x2 is the prefix
        #   2. 4x5 is the suffix
        # To compute this,
        #   1. First go through nums from L -> R:
        #       1.1. Store the prefix products at each respective positions in output array
        #   2. Then go through nums from R -> L
        #       2.2. Multiply the suffix products to the value stored at each respective position in output array and store it there
        # Determining the "respective position" is intuitive (see NeetCode explanation video or draw it out)
        # We'll require helper variables to maintain the current prefix and suffix product
        # This way we'll have O(n) time complexity (O(n + n) to be specific)
        # and O(1) space (technically O(n) due to output array but that is ignored in this problem)

        output = []
        prefix_prod = 1
        for i in range(len(nums)):
            output.append(prefix_prod)
            prefix_prod *= nums[i]

        print(output)

        suffix_prod = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= suffix_prod
            suffix_prod *= nums[i]

        return output

solution1 = Solution()
print(solution1.productExceptSelf([-1, 0, 1, 2, 3]))