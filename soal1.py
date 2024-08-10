class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_dict = {}
        
        # Iterasi melalui array nums
        for i, num in enumerate(nums):
            complement = target - num
            
            # Cek apakah komplemen sudah ada di dictionary
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

solution = Solution()

nums = [2, 7, 11, 15]
target = 9
output = solution.twoSum(nums, target)
print(output)
