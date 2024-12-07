from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # # checking if board[0]==[1,2,3] AND board[1]==[4,5,0], i'll check for the condition till then
        # steps = 0
        # while(board[0]==[1,2,3] and board[1]==[4,5,0]):
        #     # checking for element board[0][0]
        #     if board[0][0]!==1:
        #         if board[0][1]==1:
        #             board[0][1],board[0][0] = board[0][0],board[0][1]
        #             steps+=1
        #         elif board[1][0]==1:
        #             board[1][0],board[0][0] = board[0][0],board[1][0]
        #             steps+=1
        #         else:
        #             return -1

        #         # checking for element board[0][1]
        #         if board[0][1]!=2:
        #             if board[0][0]==2:
        #                 board[0][1],board[0][0] = board[0][0],board[0][1]
        #                 steps+=1
        #             elif board[0][2]==2:
        #                 board[0][1],board[0][2] = board[0][2],board[0][1]
        #                 steps+=1
        #             elif board[1][1]==2:
        #                 board[0][1],board[1][1] = board[1][1],board[0][1]
        #                 steps+=1
        #             else:
        #                 return -1

        #         # checking for element board[0][2]
        #         if board[0][2]!=3:
        #             if board[0][1]==3:
        #                 board[0][1],board[0][2] = board[0][2],board[0][1]
        #                 steps+=1
        #             elif board[1][2]==3:
        #                 board[1][2],board[0][2] = board[0][2],board[1][2]
        #                 steps+=1
        #             else:
        #                 return -1

        #         # checking for element board[1][0]
        #         if board[1][0]!=4:
        #             if board[0][0]==4:
        #                 board[0][0],board[1][0] = board[1][0],board[0][0]
        #                 steps+=1
        #             elif board[1][1]==4:
        #                 board[1][1],board[1][0] = board[1][0],board[1][1]
        #                 steps+=1
        #             else:
        #                 return -1
                
        #         # checking for element board[1][1]
        #         if board[1][1]!=5:
        #             if board[1][0]==5:
        #                 board[1][0],board[1][1] = board[1][1],board[1][0]
        #                 steps+=1
        #             elif board[0][1]==5:
        #                 board[0][1],board[1][1] = board[1][1],board[0][1]
        #                 steps+=1
        #             elif board[1][2]==5:
        #                 board[1][2],board[1][1] = board[1][1],board[1][2]
        #                 steps+=1
        #             else:
        #                 return -1
                
        #         # checking for element board[0][2]
        #         if board[0][2]!=3:
        #             if board[0][1]==3:
        #                 board[0][1],board[0][2] = board[0][2],board[0][1]
        #                 steps+=1
        #             elif board[1][2]==3:
        #                 board[1][2],board[0][2] = board[0][2],board[1][2]
        #                 steps+=1
        #             else:
        #                 return -1

        # Convert board to a string for easier state management
        start = ''.join(str(num) for row in board for num in row)
        target = "123450"
        
        # Adjacency list for 2x3 board
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        # BFS setup
        queue = deque([(start, start.index('0'), 0)])  # (state, zero_position, moves)
        visited = set()
        visited.add(start)
        
        while queue:
            state, zero_pos, moves = queue.popleft()
            
            # Check if target is reached
            if state == target:
                return moves
            
            # Explore neighbors
            for neighbor in neighbors[zero_pos]:
                # Swap zero with its neighbor
                new_state = list(state)
                new_state[zero_pos], new_state[neighbor] = new_state[neighbor], new_state[zero_pos]
                new_state = ''.join(new_state)
                
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, neighbor, moves + 1))
        
        # If we exhaust the queue, the puzzle is unsolvable
        return -1
                
                
                


