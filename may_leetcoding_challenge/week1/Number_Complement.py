'''
[476] Number Complement

https://leetcode.com/problems/number-complement/description/


Testcase Example:  '5'

Given a positive integer, output its complement number. The complement
strategy is to flip the bits of its binary representation.



Example 1:


Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits),
and its complement is 010. So you need to output 2.


Example 2:


Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and
its complement is 0. So you need to output 0.

Note:


The given integer is guaranteed to fit within the range of a 32-bit signed
integer.
You could assume no leading zero bit in the integer’s binary
representation.
This question is the same as 1009:
https://leetcode.com/problems/complement-of-base-10-integer/
'''


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i=1
        while i<=num:
            i=i<<1
        return (i-1)^ num




'''

Good Explaination : https://leetcode.com/problems/complement-of-base-10-integer/discuss/613118/two-approaches%3A-bitwise-operation-and-math-formular
Explaination : 

Example:
5 = 101
mask = 1
shift mask left while shifting a copy of 5 right until it is 0
mask << 1 == 10
101 >> 1 == 10
mask << 1 == 100
10 >> 1 == 1
mask << 1 == 1000
1 >> 1 == 0

finally, mask - 1 == 1000 - 1 == 8 - 1 == 111
111 ^ 101
^ sets any of the same bits to 0
result = 010
'''