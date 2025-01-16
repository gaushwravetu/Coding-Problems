class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1),len(nums2)
        freq_dict = {}
        for i in nums1:
            if i not in freq_dict:
                freq_dict[i]=m
            else:
                freq_dict[i]+=m
        
        for j in nums2:
            if j not in freq_dict:
                freq_dict[j]=n
            else:
                freq_dict[j]+=n
        # print(freq_dict)
        result = 0
        for i in freq_dict:
            if freq_dict[i]%2!=0:
                result = result^i
        return result
        