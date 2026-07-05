class Solution:
    def threeSum(self, nums: List[int])-> List[List[int]]:

        nums.sort()

        answer = []

        for i in range(len(nums)):

            # Skip duplicate starting numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue #breaks loop and stops if consectuive nums are the same

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:

                    answer.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return answer