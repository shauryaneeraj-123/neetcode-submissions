class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Store every number in a set for O(1) lookups.
        num_set = set(nums)

        # Stores the length of the longest consecutive sequence found.
        longest = 0

        # Check every number in the set.
        for num in num_set:

            # If the previous number exists,
            # then this is NOT the start of a sequence.
            if num - 1 not in num_set:

                # Current number is the start of a new sequence.
                length = 1

                # Continue checking the next consecutive numbers.
                while num + length in num_set:
                    length += 1

                # Update the longest sequence found so far.
                longest = max(longest, length)

        # Return the length of the longest consecutive sequence.
        return longest