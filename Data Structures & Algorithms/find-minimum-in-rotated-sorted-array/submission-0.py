class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #BRUTE FORCE

        minimum = nums[0]

        for num in nums: 
            minimum= min(minimum, num)

        return minimum