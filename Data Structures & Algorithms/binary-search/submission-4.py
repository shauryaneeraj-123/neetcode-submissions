class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            # Find the middle of the current search range.
            m = (l + r) // 2

            # Found the target.
            if nums[m] == target:
                return m

            # Target is larger, so search the right half.
            elif nums[m] < target:
                l = m + 1

            # Target is smaller, so search the left half.
            else:
                r = m - 1

        # Target was not found.
        return -1