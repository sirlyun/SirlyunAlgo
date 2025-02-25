'''
    indices of the two numbers such that they add up to target
    each input would have exactly one solution
    may not use the same element twice
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)

        num_dict = {}
        for idx, value in enumerate(nums):
            if (target - value) in num_dict.keys():
                return sorted([idx, num_dict[(target - value)]])

            num_dict[value] = idx