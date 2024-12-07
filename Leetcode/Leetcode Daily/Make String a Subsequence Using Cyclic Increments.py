class Solution:
    def canMakeSubsequence(self, s1: str, s2: str) -> bool:
        i,j,s1_len,s2_len = 0,0,len(s1),len(s2)
        flag_list = [False]*s2_len
        if s2_len>s1_len:
            return False
        while(i<s1_len and j<s2_len):
                if s1[i]==s2[j]:
                    flag_list[j]=True
                    i+=1
                    j+=1
                elif s1[i]!=s2[j]:
                    next_char = chr((ord(s1[i]) - ord('a') + 1) % 26 + ord('a'))
                    # print(next_char,s2[j])
                    if next_char==s2[j]:
                        flag_list[j]=True
                        i+=1
                        j+=1
                    else:
                        i+=1
        # flag_list = set(flag_list)
        if all(flag_list)==False:
            return False
        return True


        
        