Find the Number of Distinct Colors Among the Balls
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_dict,colour_dict = {},{}
        result = []
        prev_colour,count = float('-inf'),0
        for ball,colour in queries:

            if ball not in ball_dict:
                ball_dict[ball]=colour
            else:
                prev_colour = ball_dict[ball]
                colour_dict[prev_colour]-=1

                if colour_dict[prev_colour]==0:
                    del colour_dict[prev_colour]

            ball_dict[ball]=colour
        
            if colour not in colour_dict:
                colour_dict[colour]=1
            else:
                colour_dict[colour]+=1

            result.append(len(colour_dict))

        return result
            
