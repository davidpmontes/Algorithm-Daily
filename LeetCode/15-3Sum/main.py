class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == None or len(nums) < 3:
            return []
        
        nums.sort()
        s = set()
        answer = []
        
        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                elif total == 0:
                    if ((nums[i], nums[j], nums[k])) not in s:
                        s.add((nums[i], nums[j], nums[k]))
                        answer.append([nums[i], nums[j], nums[k]])
                    j += 1
        return answer
