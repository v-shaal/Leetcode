# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#
#

# @lc code=start
import operator


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ele = {}

        for i in nums:
            if i in ele.keys():
                ele[i] += 1

            else:
                ele[i] = 1
            if ele[i] > n / 2:
                return i


# more Efficeient Approach

class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            else:
                if nums[i] == candidate:
                    count += 1
                else:
                    count -= 1

        return candidate
