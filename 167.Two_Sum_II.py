# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Note: try to reduce running time for some extreme cases (long input)

class Solution(object):
    """ solution that are not optimized
    def twoSum(self, numbers, target):
        if (len(numbers) < 2):
            return None
        for i, x in enumerate(numbers):
            for j, y in enumerate(numbers[i+1:]):
                if ((x+y) == target):
                    return i+1, i+1+j+1
                if ((x + y) > target):
                    break
        return None
    """
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    # beat 60%
    def twoSum(self, numbers, target):
        if numbers is None or len(numbers) < 2:
            return None
        i = 0
        j = len(numbers)-1
        while i != j:
            if numbers[i] + numbers[j] == target:
                return i+1, j+1
            elif numbers[i] + numbers[j] > target:
                j-=1
            else:
                i+=1
        return None

if __name__ == "__main__":
    s = Solution()
    #numbers = [2,3,4]
    #target = 6
    numbers = [2, 7, 11, 15]
    target = 9
    print (s.twoSum(numbers, target))