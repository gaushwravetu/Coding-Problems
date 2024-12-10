class Solution:
    def maximumLength(self, s: str) -> int:
        mydict = {}
        slen,i = len(s),0
        # mydict[s[0]]=1
        mymax = -1
        # while(i<slen-1):
        #     if s[i] in mydict:
        #         mydict[s[i]]+=1
        #     else:
        #         mydict[s[i]]=1
        #     j = i+1
        #     while(j<slen and i<j):
        #         if s[i]!=s[j]:
        #             if s[j] in mydict:
        #                 mydict[s[j]]+=1
        #             else:
        #                 mydict[s[j]]=1
        #             i+=1
        #             print(mydict)
        #             break
        #         else:
        #             # if s[j] in mydict:
        #             #     mydict[s[j]]+=1
        #             # else:
        #             #     mydict[s[j]]=1
        #             if s[i:j+1] in mydict:
        #                 mydict[s[i:j+1]]+=1
        #             else:
        #                 mydict[s[i:j+1]]=1
        #             j+=1
        #     i+=1
        # print(mydict)
        # for i in mydict:
        #     if mydict[i]>=3:
        #         mymax = max(mymax,len(i))
        # return mymax

        # Brute Force approach
        for i in range(slen):
            curr_string = ""
            for j in range(i,slen):
                if s[i]==s[j]:
                    curr_string+=s[j]
                    if curr_string in mydict:
                        mydict[curr_string]+=1
                    else:
                        mydict[curr_string]=1
                else:
                    break
        for i in mydict:
            if mydict[i]>=3:
                mymax = max(mymax,len(i))
        return mymax
        
            
        