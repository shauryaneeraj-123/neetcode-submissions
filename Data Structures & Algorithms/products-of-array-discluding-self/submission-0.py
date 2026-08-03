class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Create the output array and initialize every value to 1.
        output = [1] * len(nums)

        # Stores the product of all numbers to the left
        # of the current index.
        prefix = 1

        # First pass (Left → Right):
        # Fill each position with the product of all numbers
        # to its left.
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        # Stores the product of all numbers to the right
        # of the current index.
        postfix = 1

        # Second pass (Right → Left):
        # Multiply each position by the product of all numbers
        # to its right.
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        # Return the final product array.
        return output