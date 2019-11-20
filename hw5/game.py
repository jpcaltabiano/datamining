#-------------------------------------------------------------------------
from abc import ABC, abstractmethod
import numpy as np
#-------------------------------------------------------------------------


#-------------------------------------------------------
class BoardGame(ABC):
    '''
       This is the parent class of all board games. It defines the basic interface (APIs) that each board game class should provide. 
    '''

    # ----------------------------------------------
    @abstractmethod
    def initial_game_state(self):
        '''
           Create an initial game state.  
            Return:
                s: the initial state of the game, an integer matrix (TicTacToe: shape 3 by 3, Othello: 8 by 8)
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X". 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the "O".
        '''
        pass


    # ----------------------------------------------
    @abstractmethod
    def check_valid_move(self,s,r,c,x):
        '''
            check if a move is valid or not.
            Return True if valid, otherwise return False.
            Input:
                s: the current state of the game, an integer matrix.
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X" player. 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by "O" player.
                r: the row number of the move
                c: the column number of the move
                x: the role of the player, 1 if you are the "X" player in the game
                        -1 if you are the "O" player in the game. 
            Outputs:
                valid: boolean scalar, True (if the move is valid), otherwise False 
        '''
        pass

    # ----------------------------------------------
    @abstractmethod
    def get_valid_moves(self, s,x):
        '''
           Get a list of available (valid) next moves from a game state.  
            Input:
                s: the current state of the game, an integer matrix (TicTacToe: shape 3 by 3, Othello: 8 by 8)
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X". 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the "O".
                    For example, in TicTacToe game, the following game state 
                     | X |   | O |
                     | O | X |   |
                     | X |   | O |
                    is represented as the following numpy matrix in game state
                    s= [[ 1 , 0 ,-1 ],
                        [-1 , 1 , 0 ],
                        [ 1 , 0 ,-1 ]]
               x: who's turn in this step of the game, x=1 if it is "X" player's turn. 
                    x=-1 if it's "O" player's turn. 
            Outputs:
                m: a list of possible next moves, where each next move is a (r,c) tuple, 
                   r denotes the row number, c denotes the column number. 
            For example, for the following game state, 
                    s= [[ 1 , 0 ,-1 ],
                        [-1 , 1 , 0 ],
                        [ 1 , 0 ,-1 ]]
            the valid moves are the empty grid cells: 
                (r=0,c=1) --- the first row, second column 
                (r=1,c=2) --- the second row, the third column 
                (r=2,c=1) --- the third row , the second column
            So the list of valid moves is m = [(0,1),(1,2),(2,1)]
        '''
        pass

    # ----------------------------------------------
    @abstractmethod
    def check_game(self,s):
        '''
            check if the game has ended or not. 
            If yes (game ended), return the game result (1: x_player win, -1: o_player win, 0: draw)
            If no (game not ended yet), return None 
            
            Input:
                s: the current state of the game, an integer matrix (TicTacToe: shape 3 by 3, Othello: 8 by 8)
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X" player. 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by "O" player.
            Outputs:
                e: the result, an integer scalar with value 0, 1 or -1.
                    if e = None, the game has not ended yet.
                    if e = 0, the game ended with a draw.
                    if e = 1, X player won the game.
                    if e = -1, O player won the game.
        '''
        pass

    # ----------------------------------------------
    @abstractmethod
    def apply_a_move(self,s,r,c,x):
        '''
            Apply a move of a player to the game and change the game state accordingly. 
            Input:
                s: the current state of the game, an integer matrix (TicTacToe: shape 3 by 3, Othello: 8 by 8)
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X" player. 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by "O" player.
                r: the row number of the move, an integer scalar.
                c: the column number of the move, an integer scalar.
                x: who's turn in this step of the game, x=1 if it is "X" player's turn. 
                    x=-1 if it's "O" player's turn. 
            Output:
                nx: in the next step of the game, who's is it?, x=1 if it is "X" player's turn, otherwise -1.

            For example, in TicTacToe, suppose the current game state is:
                    s=[[ 0, 1, 1],
                       [ 0,-1,-1],
                       [ 1,-1, 1]]
            and it's "O" player's turn.
            If the "O" player chooses the move (r=1,c=0), then after applying the move on the board,
            the game state becomes:
                    s=[[ 0, 1, 1],
                       [-1,-1,-1],
                       [ 1,-1, 1]]
        '''
        pass

    # ----------------------------------------------
    def run_a_game(self,x_player,o_player,s=None,x=1):
        '''
            run a game starting from the game state (s), letting X and O players to play in turns, until the game ends.
            When the game ends, return the result of the game.
            Input:
                s: the initial state of a game, an integer matrix of shape 3 by 3. 
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X" player. 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by "O" player.
                x_player: the "X" player 
                o_player: the "O" player 
                x: who moves first in the game (by default, X player moves first in a game). 
            Outputs:
                e: the result of the game, an integer scalar with value 0, 1 or -1.
                    if e = 0, the game ends with a draw/tie.
                    if e = 1, X player won the game.
                    if e = -1, O player won the game.
        '''
        # if the initial game state is not given, use the empty board as the starting state
        if s is None:
            s=self.initial_game_state()
        else: # if s is assigned, start the game from the given game state s
            s=s.copy()

        # start the game: 
        for _ in range(1000):
            e = self.check_game(s) # check if the game has ended already
            if e is not None: # if the game has ended, stop the game and return the result
                break
            if x==1:
                r,c = x_player.choose_a_move(self,s,x) # "X" player choose a move
            else:
                r,c = x_player.choose_a_move(self,s,x) # "O" player choose a move
            assert self.check_valid_move(s,r,c,x) # the move must be valid
            x=self.apply_a_move(s,r,c,x) # apply the move and update game state 
        return e


#-------------------------------------------------------------------------
'''
    Othello is a larger board game than TicTacToe: https://en.wikipedia.org/wiki/Reversi 
    For a demo of the Othello game, you could visit: https://hewgill.com/othello/ 
    or https://www.mathsisfun.com/games/reversi.html  (for playing with an AI)
'''

#-------------------------------------------------------
class Othello(BoardGame):
    '''
        Othello game engine: the goal is to provide a platform for two AI players to play the game in turns and return the game result. 
    '''
    # ----------------------------------------------
    def initial_game_state(self):
        '''
           Create an initial game state.  
            Return:
                s: the initial state of the game, an integer matrix (8 by 8)
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X". 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the "O".
        '''
        s = np.zeros((8,8))
        s[3,3]= 1
        s[3,4]=-1
        s[4,3]=-1
        s[4,4]= 1
        return s

    # ----------------------------------------------
    def check_valid_move(self,s,r,c,x):
        '''
            check if a move is valid or not.
            Return True if valid, otherwise return False.
            Input:
                s: the current state of the game, an integer matrix of shape 8 by 8. 
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X" player. 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by "O" player.
                r: the row number of the move
                c: the column number of the move
                x: the role of the player, 1 if you are the "X" player in the game
                        -1 if you are the "O" player in the game. 
            Outputs:
                valid: boolean scalar, True (if the move is valid), otherwise False 
        '''
        # the cell must be empty
        if s[r,c]!=0:
            return False
        # a move is valid only if it can flip at least one stone in any of the 8 directions
        # 8 directions to check if there is a possible flip
        direction =[( 1, 0),(-1, 0),
                    ( 0, 1),( 0,-1),
                    ( 1, 1),(-1,-1),
                    ( 1,-1),(-1, 1)]
        nx=-x
        # check 8 directions
        for ri,ci in direction:
            found_nx=False
            # check one direction
            for i in range(1,8):
                a=r+ri*i
                b=c+ci*i
                if a<0 or a>7 or b<0 or b>7: # out of the board
                    break
                if found_nx:
                    if s[a][b]==x: 
                        return True # valid (found a flip)
                    if s[a][b]==0:
                        break
                elif s[a][b]==nx: # found one
                        found_nx=True
                else:
                    break
        return False


    # ----------------------------------------------
    def get_valid_moves(self,s,x):
        '''
           Get a list of available (valid) next moves from a game state of Othello 
         
            Input:
                s: the current state of the game, an integer matrix of shape 8 by 8. 
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X" player. 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by "O" player.
                    x: who's turn in this step of the game, 1 if "X" player's turn.
                        -1 if "O" player's turn. 
            Outputs:
                m: a list of possible next moves, where each next move is a (r,c) tuple, 
                   r denotes the row number, c denotes the column number. 
            For example, suppose we have the following game state and it is "X" player's turn (x=1):
                    s= [[ 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0,-1,-1,-1, 1, 0],
                        [ 0, 0, 0, 1, 1, 1, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0]]
            The valid moves are the empty grid cells, where at least one "O" player's stone can be flipped. 
            They are marked as "*": 
                       [[ 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, *, *, *, *, *, 0],
                        [ 0, 0, *,-1,-1,-1, 1, 0],
                        [ 0, 0, 0, 1, 1, 1, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0],
                        [ 0, 0, 0, 0, 0, 0, 0, 0]]
            In the example, the valid next moves are
                (r=2,c=2) --- the third row, third column 
                (r=2,c=3) --- the third row, fourth column 
                (r=2,c=4) --- the third row, fifth column
                (r=2,c=5) --- the third row, sixth column
                (r=2,c=6) --- the third row, seventh column
                (r=3,c=2) --- the fourth row, third column
            So the list of valid moves is m = [(2,2),(2,3),(2,4),(2,5),(2,6),(3,2)]
        '''
        rs,cs=np.where(s==0) 
        e = list(zip(rs,cs)) #empty slots
        m = []
        for r,c in e:
            if self.check_valid_move(s,r,c,x):
                m.append((r,c))
        return m


    # ----------------------------------------------
    def check_game(self,s):
        '''
            check if the game has ended or not. 
            If yes (game ended), return the game result (1: x_player win, -1: o_player win, 0: draw)
            If no (game not ended yet), return None 
            
            Input:
                s: the current state of the game, an integer matrix of shape 8 by 8. 
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X" player. 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by "O" player.
            Outputs:
                e: the result, an integer scalar with value 0, 1 or -1.
                    if e = None, the game has not ended yet.
                    if e = 0, the game ended with a draw.
                    if e = 1, X player won the game.
                    if e = -1, O player won the game.
        '''
        # if neither player has a valid move, the game ends
        if len(self.get_valid_moves(s,x=1))==0 and len(self.get_valid_moves(s,x=-1))==0:
            nx = np.sum(s==1)
            no = np.sum(s==-1)
            # the player with the most stones wins
            if nx>no:
                e=1
            elif nx<no:
                e=-1
            else:
                e=0
        else:
            e=None
        return e

    # ----------------------------------------------
    def apply_a_move(self,s,r,c,x):
        '''
            Apply a move of a player to the Othello game and change the game state accordingly. 
            Here we assume the move is valid.
            
            Input:
                s: the current state of the game, an integer matrix of shape 3 by 3. 
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X" player. 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by "O" player.
                r: the row number of the move
                c: the column number of the move
                x: the role of the player, 1 if you are the "X" player in the game
                        -1 if you are the "O" player in the game. 
        '''
        s[r,c]=x 
        # 8 directions to check
        direction =[( 1, 0),(-1, 0),
                    ( 0, 1),( 0,-1),
                    ( 1, 1),(-1,-1),
                    ( 1,-1),(-1, 1)]
        nx=-x
        f = []
        # flip 8 directions
        for ri,ci in direction:
            found_nx=False
            l=[]
            # flip one direction
            for i in range(1,8):
                a=r+ri*i
                b=c+ci*i
                if a<0 or a>7 or b<0 or b>7: # out of the board
                    break
                if found_nx:
                    if s[a][b]==x: 
                        for li in l:
                            f.append(li)
                        break 
                    elif s[a][b]==0:
                        break
                    else:
                        l.append((a,b))
                elif s[a][b]==nx: # found one
                        found_nx=True
                        l.append((a,b))
                else:
                    break
        for ri,ci in f:
            s[ri,ci]=x
        # determine who's turn in the next step of the game
        if len(self.get_valid_moves(s,-x))>0:
            return -x
        else:
            return x




#-------------------------------------------------------
class Player(ABC):
    '''
       This is the parent class of all board game players. It defines the basic interface (APIs) that each player class should provide. 
    '''

    # ----------------------------------------------
    @abstractmethod
    def choose_a_move(self,g,s,x):
        '''
            The action function, which chooses one random valid move in each step of the game.  
            This function will be called by the game at each game step.
            For example, suppose we have 2 random players (say A and B) in a game.
            The game will call the choose_a_move() function of the two players in turns as follows:

            Repeat until game ends:
                (1) r,c = A.choose_a_move(game,game_state, x=1 ) --- "X" player (A) choose a move
                (2) the game updates its game state 
                (3) r,c = B.choose_a_move(game,game_state, x=-1 ) --- "O" player (B) choose a move
                (4) the game updates its game state 

            Input:
                g: the game environment being played, such as TicTacToe or Othello. 
                s: the current state of the game, an integer matrix of shape 3 by 3 (TicTacToe) or 8 by 8 (Othello). 
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X". 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the "O".
                    For example, in TicTacToe, the following game state 
                     | X |   | O |
                     | O | X |   |
                     | X |   | O |
                    is represented as the following numpy matrix
                    s= [[ 1 , 0 ,-1 ],
                        [-1 , 1 , 0 ],
                        [ 1 , 0 ,-1 ]]
               x: the role of the player, x=1 if this agent is the "X" player in the game
                    x=-1 if this agent is the "O" player in the game. 
           Outputs:
                r: the row number of the next move, an integer scalar.
                c: the column number of the next move, an integer scalar.
        '''
        pass



#-------------------------------------------------------
class DummyPlayer(Player):
    '''
        Dummy player: it always chooses the first valid move.
        This player is used for testing game engines. 
    '''
    # ----------------------------------------------
    def choose_a_move(self,g,s,x):
        '''
            The action function, which chooses one random valid move in each step of the game.  
            This function will be called by the game at each game step.
            For example, suppose we have 2 random players (say A and B) in a game.
            The game will call the choose_a_move() function of the two players in turns as follows:

            Repeat until game ends:
                (1) r,c = A.choose_a_move(game,game_state, x=1 ) --- "X" player (A) choose a move
                (2) the game updates its game state 
                (3) r,c = B.choose_a_move(game,game_state, x=-1 ) --- "O" player (B) choose a move
                (4) the game updates its game state 

            Input:
                g: the game environment being played, such as TicTacToe or Othello. 
                s: the current state of the game, an integer matrix of shape 3 by 3 (TicTacToe) or 8 by 8 (Othello). 
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X". 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the "O".
                    For example, in TicTacToe, the following game state 
                     | X |   | O |
                     | O | X |   |
                     | X |   | O |
                    is represented as the following numpy matrix
                    s= [[ 1 , 0 ,-1 ],
                        [-1 , 1 , 0 ],
                        [ 1 , 0 ,-1 ]]
               x: the role of the player, x=1 if this agent is the "X" player in the game
                    x=-1 if this agent is the "O" player in the game. 
           Outputs:
                r: the row number of the next move, an integer scalar.
                c: the column number of the next move, an integer scalar.
        '''
        m=g.get_valid_moves(s,x)
        r,c = m[0]
        return r,c




#-------------------------------------------------------------------------
'''
    GO is a famous board game, very challenging problem in AI. 
    For a demo of the Othello game, you could visit: https://online-go.com  
'''

#-------------------------------------------------------
class GO(BoardGame):
    '''
        GO game engine: the goal is to provide a platform for two AI players to play the game in turns and return the game result. 
    '''
    def __init__(self,board_size=19):
        self.board_size = board_size
    # ----------------------------------------------
    def initial_game_state(self):
        '''
           Create an initial game state.  
            Return:
                s: the initial state of the game, an integer matrix 
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X". 
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the "O".
        '''
        s = np.zeros((self.board_size,self.board_size))
        return s




