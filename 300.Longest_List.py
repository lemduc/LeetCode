#https://leetcode.com/problems/longest-increasing-subsequence/description/

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size



def stringToIntegerList(input):
    input = input.strip()
    input = input[1:-1]
    return [int(number) for number in input.split(",")]


import sys


def readlines():
    for line in sys.stdin:
        yield line.strip('\n')


def main():
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums = stringToIntegerList(line)

            ret = Solution().lengthOfLIS(nums)

            out = str(ret)
            print
            out
        except StopIteration:
            break


if __name__ == '__main__':
    #main()
    test = [10,9,2,5,3,4]
    print(Solution().lengthOfLIS(test))