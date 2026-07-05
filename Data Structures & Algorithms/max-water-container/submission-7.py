class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Best area we've found so far
        max_area = 0

        # Left pointer starts at the beginning
        left = 0

        # Right pointer starts at the end
        right = len(heights) - 1

        # Continue until the pointers meet
        while left < right:

            # Distance between the two walls
            width = right - left

            # Water height is limited by the shorter wall
            current_height = min(heights[left], heights[right])

            # Compute the current container's area
            area = width * current_height

            # Update the best area if needed
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter wall
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area