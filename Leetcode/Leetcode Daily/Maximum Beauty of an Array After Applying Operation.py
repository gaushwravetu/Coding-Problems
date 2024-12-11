class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # rangelist = []
        # result = 1
        # for i in range(n):
        #     rangelist.append((nums[i]-k, nums[i]+k))
        # rangelist.sort()
        # # print(rangelist)
        # for i in range(n):
        #     subseqcount = 1
        #     for j in range(i+1,n):
        #         if rangelist[i][1]>=rangelist[j][0]:
        #             # print(rangelist[i][1],rangelist[j][0])
        #             subseqcount+=1
        #     # print(subseqcount)
        #     result = max(result,subseqcount)
        # return result


        nums.sort()
        max_freq = 0
        left = 0

        for right in range(len(nums)):
            # Adjust range to ensure nums[right] - nums[left] <= 2 * k
            while nums[right] - nums[left] > 2 * k:
                left += 1
            # Update max frequency
            max_freq = max(max_freq, right - left + 1)

        return max_freq
        