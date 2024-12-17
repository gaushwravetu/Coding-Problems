class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Taken a list of size 26 which count the occurance of the characters
        count_char = [0]*26
        for char in s: #Time complexity - O(n)
            index = ord(char)-ord('a') #Storing the count of each char at respective indices, a->0, b->1..... so on
            count_char[index]+=1
        i = 25
        result = ""
        while(i>=0): #Time complexity - O(26) which is constant
            if count_char[i]==0:
                i-=1
                continue
            mychar =  chr(i+ord('a')) #Converting into char to know its count>=repeatLimit and appending it into my result(lexicographically)
            
            required_freq = min(count_char[i],repeatLimit)
            count_char[i]-=required_freq
            result+=mychar*required_freq

            if count_char[i]>0:
                j = i-1
                while(j>=0 and count_char[j]==0): #Time complexity - O(26) which is constant
                    j-=1
                if j>=0:    
                    mychar =  chr(j+ord('a'))
                    result+=mychar
                    count_char[j]-=1
                else:
                    break
        return result

