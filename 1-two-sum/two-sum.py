class Solution:
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]  # Found a pair
            num_dict[num] = i  # Store the current number and its index

        # If no solution is found, return an empty list or raise an exception
        return []