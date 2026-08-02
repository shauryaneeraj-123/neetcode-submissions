class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Stores all unique characters currently inside our sliding window.
        seen = set()

        # Left pointer marks the beginning of the current window.
        left = 0

        # Stores the length of the longest valid substring found so far.
        longest = 0

        # Expand the window one character at a time using the right pointer.
        for right in range(len(s)):

            # If the current character already exists in the window,
            # shrink the window from the left until the duplicate is removed.
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add the current character now that the window is valid again.
            seen.add(s[right])

            # Update the longest substring length if the current window is larger.
            longest = max(longest, right - left + 1)

        # Return the length of the longest substring without duplicates.
        return longest