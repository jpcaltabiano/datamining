from problem1 import *
from game import Othello 
import numpy as np
import sys

'''
    Unit test 1:
    This file includes unit tests for problem1.py.
    You could test the correctness of your code by typing `nosetests -v test1.py` in the terminal.
'''

#-------------------------------------------------------------------------
def test_terms_and_conditions():
    ''' Read and Agree with Terms and Conditions'''
    assert Terms_and_Conditions() # require reading and agreeing with Terms and Conditions. 


#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 1 (50 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)


#-------------------------------------------------------------------------
def test_get_valid_moves():
    '''(5 points) get_valid_moves()'''
    g = TicTacToe()  # game 

    s=np.array([[  1 , 0 ,-1 ],
                [ -1 , 1 , 0 ],
                [  1 , 0 ,-1 ]])
    m=g.get_valid_moves(s)
    assert type(m)==list
    assert len(m)==3
    assert m[0]== (0,1) or m[0]== (1,2) or m[0] == (2,1)
    assert m[1]== (0,1) or m[1]== (1,2) or m[1] == (2,1)
    assert m[2]== (0,1) or m[2]== (1,2) or m[2] == (2,1)
    assert m[0]!=m[1] and m[1]!=m[2]

    
    m=g.get_valid_moves(np.zeros((3,3)))
    assert len(m)==9

    s=np.array([[  1 , 0 ,-1 ],
                [  0 , 0 , 0 ],
                [  1 , 0 ,-1 ]])
    m=g.get_valid_moves(s)
    assert len(m)==5
    for i in m:
        assert i== (0,1) or i== (1,0) or i== (1,1) or i== (1,2) or i== (2,1)  


#-------------------------------------------------------------------------
def test_check_game():
    '''(5 points) check_game()'''
    g = TicTacToe()  # game 
    s=np.array([[ 1, 0, 1],
                [ 0, 0,-1],
                [ 0,-1, 0]])
    e = g.check_game(s)
    assert e is None # the game has not ended yet

    s=np.array([[ 1,-1, 1],
                [ 0, 1,-1],
                [-1, 1,-1]])
    e = g.check_game(s)
    assert e is None # the game has not ended yet

    s=np.array([[ 1, 1, 1],
                [ 0, 0,-1],
                [ 0,-1, 0]])
    e = g.check_game(s)
    assert e == 1  # x player wins
    e = g.check_game(-s)
    assert e ==-1  # O player wins

    s=np.array([[-1, 0, 0],
                [ 1, 1, 1],
                [ 0,-1, 0]])
    e = g.check_game(s)
    assert e == 1  # x player wins
    e = g.check_game(-s)
    assert e ==-1  # O player wins

    s=np.array([[-1, 0, 0],
                [ 0, 0,-1],
                [ 1, 1, 1]])
    e = g.check_game(s)
    assert e == 1  # x player wins
    e = g.check_game(-s)
    assert e ==-1  # O player wins
    
    s=np.array([[ 1, 0, 0],
                [ 1, 0,-1],
                [ 1,-1, 0]])
    e = g.check_game(s)
    assert e == 1  # x player wins
    e = g.check_game(-s)
    assert e ==-1  # O player wins

    s=np.array([[-1, 1, 0 ],
                [ 0, 1, 0 ],
                [-1, 1, 0 ]])
    e = g.check_game(s)
    assert e == 1  # x player wins
    e = g.check_game(-s)
    assert e ==-1  # O player wins

    s=np.array([[-1, 0, 1],
                [ 0, 0, 1],
                [-1, 0, 1]])
    e = g.check_game(s)
    assert e == 1  # x player wins
    e = g.check_game(-s)
    assert e ==-1  # O player wins

    s=np.array([[ 1, 0, 0],
                [ 0, 1,-1],
                [-1, 0, 1]])
    e = g.check_game(s)
    assert e == 1  # x player wins
    e = g.check_game(-s)
    assert e ==-1  # O player wins

    s=np.array([[-1, 0, 1],
                [ 0, 1, 0],
                [ 1, 0,-1]])
    e = g.check_game(s)
    assert e == 1  # x player wins
    e = g.check_game(-s)
    assert e ==-1  # O player wins


    s=np.array([[-1, 1,-1],
                [ 1, 1,-1],
                [ 1,-1, 1]])
    e = g.check_game(s)
    assert e == 0 # a tie



#-------------------------------------------------------------------------
def test_apply_a_move():
    '''(5 points) apply_a_move()'''
    g = TicTacToe()  # game 
    s=np.array([[ 0, 1, 1],
                [ 0,-1,-1],
                [ 1,-1, 1]]) # it's O player's turn
    g.apply_a_move(s,1,0,-1)
    n=np.array([[ 0, 1, 1],
                [-1,-1,-1],
                [ 1,-1, 1]])
    assert np.allclose(s,n)

    s=np.array([[ 0, 1, 1],
                [ 0,-1,-1],
                [ 0,-1, 1]]) # it's X player's turn
    g.apply_a_move(s,2,0,1)
    n=np.array([[ 0, 1, 1],
                [ 0,-1,-1],
                [ 1,-1, 1]])
    assert np.allclose(s,n)




#-------------------------------------------------------------------------
def test_choose_a_move():
    '''(5 points) random choose_a_move()'''

    # Game: TicTacToe
    g = TicTacToe()  # game 
    p = RandomPlayer()
    s=np.array([[ 0, 1, 1],
                [ 1, 0,-1],
                [ 1, 1, 0]])

    s_=np.array([[ 0, 1, 1],
                 [ 1, 0,-1],
                 [ 1, 1, 0]])
    count=np.zeros(3)
    for _ in range(100):
        r,c = p.choose_a_move(g,s,x=1)
        assert s[r,c]==0 # player needs to choose a valid move 
        assert np.allclose(s,s_) # the player should never change the game state object
        assert r==c # in this example the valid moves are on the diagonal of the matrix
        assert r>-1 and r<3
        count[c]+=1
    assert count[0]>20 # the random player should give roughly equal chance to each valid move
    assert count[1]>20
    assert count[2]>20
    
    s=np.array([[ 1, 1, 0],
                [ 1, 0,-1],
                [ 0, 1, 1]])

    for _ in range(100):
        r,c = p.choose_a_move(g,s,x=1)
        assert s[r,c]==0 
        assert r==2-c 
        assert r>-1 and r<3


    # The AI agent should be compatible with both games: TicTacToe and Othello.
    # now let's test on the game "Othello":
    g = Othello()  # game 
    s=np.array([[ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0,-1,-1,-1, 0, 0],
                [ 0, 0, 0, 1, 1, 1, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    p = RandomPlayer()
    s_= s.copy()
    count = np.zeros(5)
    for _ in range(200):
        r,c = p.choose_a_move(g,s,x=1)
        assert np.allclose(s,s_) # the player should never change the game state object
        assert s[r,c]==0 # player needs to choose a valid move 
        assert r==2 
        assert c>1 and c<7
        count[c-2]+=1
    assert count[0]>20 # the random player should give roughly equal chance to each valid move
    assert count[1]>20
    assert count[2]>20
    assert count[3]>20
    assert count[4]>20



    # test whether we can run a game using random player
    s=np.array([[ 0, 0,-1, 1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    for i in range(10):
        e = g.run_a_game(p,p,s=s,x=1)
        assert e==-1



    s=np.array([[ 0,-1, 1,-1, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    w=0
    for i in range(10):
        e = g.run_a_game(p,p,s=s,x=1)
        w+=e
    assert np.abs(w)<9



#-------------------------------------------------------------------------
def test_expand():
    '''(5 points) expand'''
    #---------------------
    # Game: TicTacToe
    g = TicTacToe()  # game 

    # Current Node (root)
    s=np.array([[0, 1,-1],
                [0,-1, 1],
                [0, 1,-1]])
    n = MMNode(s,x=1) #it's X player's turn
    # expand
    n.expand(g)
    assert len(n.c) ==3 
    assert n.x==1
    s_=np.array([[0, 1,-1],
                 [0,-1, 1],
                 [0, 1,-1]])
    # the current game state should not change after expanding
    assert np.allclose(n.s,s_) 
    for c in n.c:
        assert type(c)==MMNode
        assert c.x==-1
        assert c.p==n
        assert c.c==[] #only add one level of children nodes, not two levels.
        assert c.v==None

    # child node A
    s=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,0)
    assert c

    # child node B
    s=np.array([[ 0, 1,-1],
                [ 1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(1,0)
    assert c

    # child node C
    s=np.array([[ 0, 1,-1],
                [ 0,-1, 1],
                [ 1, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(2,0)
    assert c

    #--------------------------

    # Current Node (root)
    s=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [ 0, 1,-1]])
    n = MMNode(s,-1) #it's O player's turn
    n.expand(g)
    assert n.x==-1
    assert len(n.c) ==2
    for c in n.c:
        assert c.x==1
        assert c.p==n
        assert c.c==[]

    # child node A
    s=np.array([[ 1, 1,-1],
                [-1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(1,0)
    assert c

    # child node B
    s=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [-1, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(2,0)
    assert c

    #---------------------------
    n = MMNode(np.zeros((3,3)),1)
    n.expand(g)
    assert n.x==1
    assert len(n.c) ==9
    for c in n.c:
        assert c.x==-1
        assert c.p==n
        assert c.c==[]
        assert np.sum(c.s)==1
        assert c.v==None

    # The AI agent should be compatible with both games: TicTacToe and Othello.
    # now let's test on the game "Othello":

    #---------------------
    # Game: Othello 
    g = Othello()  # game 
    s=np.array([[ 0,-1, 1,-1, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    s_=s.copy()
    n = MMNode(s,x=1) #it's X player's turn
    # expand
    n.expand(g)
    assert len(n.c) ==2 
    assert n.x==1
    # the current game state should not change after expanding
    assert np.allclose(n.s,s_) 
    for c in n.c:
        assert type(c)==MMNode
        assert c.p==n
        assert c.c==[]
        assert c.v==None

    # child node A
    s=np.array([[ 1, 1, 1,-1, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])

    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,0)
            assert x.x==1 # it is still X player's turn because there is no valid move for O player
    assert c

    # child node B
    s=np.array([[ 0,-1, 1, 1, 1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])

    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,4)
            assert x.x==-1 
    assert c


    
    #---------------------
    s=np.array([[ 0, 1,-1, 1, 0, 0, 0, 0],
                [ 0, 0, 1, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    s_=s.copy()
    n = MMNode(s,x=-1) #it's O player's turn
    # expand
    n.expand(g)
    print(n.c)
    assert len(n.c) ==3 
    assert n.x==-1
    # the current game state should not change after expanding
    assert np.allclose(n.s,s_) 
    for c in n.c:
        assert type(c)==MMNode
        assert c.p==n
        assert c.c==[]
        assert c.v==None

    # child node A
    s=np.array([[-1,-1,-1, 1, 0, 0, 0, 0],
                [ 0, 0, 1, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])

    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,0)
            assert x.x == -1 # no valid move for X player
    assert c

    # child node B
    s=np.array([[ 0, 1,-1,-1,-1, 0, 0, 0],
                [ 0, 0, 1, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])

    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,4)
            assert x.x == 1 
    assert c

    # child node C
    s=np.array([[ 0, 1,-1, 1, 0, 0, 0, 0],
                [ 0, 0,-1, 0, 0, 0, 0, 0],
                [ 0, 0,-1, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])

    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(2,2)
            assert x.x == 1 
    assert c


#-------------------------------------------------------------------------
def test_build_tree():
    '''(5 points) build_tree'''
    #---------------------
    # Game: TicTacToe
    g = TicTacToe()  # game 

    # current node (root node)
    s=np.array([[ 0, 1,-1],
                [ 0,-1, 1],
                [ 0, 1,-1]])
    s_ = s.copy()
    n = MMNode(s, x=1) # it's X player's turn
    n.build_tree(g)

    # the current game state should not change after building the tree 
    assert np.allclose(s,s_)
    assert len(n.c) ==3 
    assert n.x==1
    assert n.v==None
    assert n.p==None
    assert n.m==None

    assert np.allclose(n.s,s_) 
    for c in n.c:
        assert type(c)==MMNode
        assert c.x==-1
        assert c.p==n
        assert len(c.c)==2
        assert c.v==None

    #-----------------------
    # child node A
    s=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,0)
            ca=x
    assert c

    # child node B
    s=np.array([[ 0, 1,-1],
                [ 1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(1,0)
            cb=x
    assert c

    # child node C
    s=np.array([[ 0, 1,-1],
                [ 0,-1, 1],
                [ 1, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(2,0)
            cc=x
    assert c

    #-----------------------
    # Child Node A's children
    for c in ca.c:
        assert c.x==1
        assert c.p==ca
        assert c.v==None

    # grand child node A1
    s=np.array([[ 1, 1,-1],
                [-1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in ca.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(1,0)
            assert len(x.c)==1
            #-----------------------
            # Great Grand Child Node A11
            assert x.c[0].x==-1
            assert x.c[0].p==x
            assert x.c[0].v==None
            assert x.c[0].c==[]
    assert c

    # grand child node A2
    s=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [-1, 1,-1]])
    c = False
    for x in ca.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(2,0)
            assert x.c== []
    assert c
    
    #-----------------------
    # Child Node B's children
    for c in cb.c:
        assert c.x==1
        assert c.p==cb
        assert c.c==[]
        assert c.v==None

    # grand child node B1
    s=np.array([[-1, 1,-1],
                [ 1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in cb.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,0)
    assert c

    # grand child node B2
    s=np.array([[ 0, 1,-1],
                [ 1,-1, 1],
                [-1, 1,-1]])
    c = False
    for x in cb.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(2,0)
    assert c

    #-----------------------
    # Child Node C's children
    for c in cc.c:
        assert c.x==1
        assert c.p==cc
        assert c.v==None

    # grand child node C1
    s=np.array([[-1, 1,-1],
                [ 0,-1, 1],
                [ 1, 1,-1]])
    c = False
    for x in cc.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,0)
            assert x.c== []
    assert c

    # grand child node C2
    s=np.array([[ 0, 1,-1],
                [-1,-1, 1],
                [ 1, 1,-1]])
    c = False
    for x in cc.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(1,0)
            assert len(x.c)==1
            # Great Grand Child Node C21
            assert x.c[0].x==-1
            assert x.c[0].p==x
            assert x.c[0].v==None
            assert x.c[0].c==[]
    assert c


    #-----------------------
    s=np.array([[ 0, 0, 1],
                [ 0, 1, 1],
                [-1, 0,-1]])
    n = MMNode(s,x=-1) #it's O player's turn
    n.build_tree(g)

    assert len(n.c) ==4 
    assert n.x==-1
    assert n.v==None
    assert n.p==None
    assert n.m==None
    
    s1=np.array([[-1, 0, 1],
                 [ 0, 1, 1],
                 [-1, 0,-1]])
    s2=np.array([[ 0,-1, 1],
                 [ 0, 1, 1],
                 [-1, 0,-1]])
    s3=np.array([[ 0, 0, 1],
                 [-1, 1, 1],
                 [-1, 0,-1]])
    s4=np.array([[ 0, 0, 1],
                 [ 0, 1, 1],
                 [-1,-1,-1]])

    for c in n.c:
        assert c.x== 1
        assert c.v==None
        assert c.p==n
        if np.allclose(c.s,s1):
            assert c.m == (0,0)
            assert len(c.c) ==3
        if np.allclose(c.s,s2):
            assert c.m == (0,1)
            assert len(c.c) ==3
        if np.allclose(c.s,s3):
            assert c.m == (1,0)
            assert len(c.c) ==3
        if np.allclose(c.s,s4):
            assert c.m == (2,1)
            assert c.c == [] #terminal node, no child


    # The AI agent should be compatible with both games: TicTacToe and Othello.
    # now let's test on the game "Othello":

    #---------------------
    # Game: Othello 
    g = Othello()  # game 
    s=np.array([[ 0, 0,-1, 1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    s_ = s.copy()
    n = MMNode(s, x=1) # it's X player's turn
    n.build_tree(g)

    # the current game state should not change after building the tree 
    assert np.allclose(s,s_)
    assert len(n.c) ==2 
    assert n.x==1
    assert n.v==None
    assert n.p==None
    assert n.m==None

    for c in n.c:
        assert type(c)==MMNode
        assert c.x==-1
        assert c.p==n
        assert c.v==None
        assert len(c.c)==1
    #-----------------------
    # child node A
    s=np.array([[ 0, 0,-1, 1, 1, 1, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,5)
            ca=x
    assert c

    #-----------------------
    # child node B
    s=np.array([[ 0, 1, 1, 1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,1)
            cb=x
    assert c

    #-----------------------
    # Child Node A's children
    # grand child node A1
    assert ca.c[0].p==ca
    assert ca.c[0].v==None
    assert ca.c[0].m==(0,6)
    assert ca.c[0].c==[]
    s=np.array([[ 0, 0,-1,-1,-1,-1,-1, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    assert np.allclose(ca.c[0].s,s)

    #-----------------------
    # Child Node B's children
    # grand child node B1
    assert cb.c[0].p==cb
    assert cb.c[0].v==None
    assert cb.c[0].m==(0,0)
    assert cb.c[0].c==[]
    s=np.array([[-1,-1,-1,-1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    assert np.allclose(cb.c[0].s,s)


    #------------------------------------
    s=np.array([[ 0,-1, 1, 1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    s_ = s.copy()
    n = MMNode(s, x=1) # it's X player's turn
    n.build_tree(g)

    # the current game state should not change after building the tree 
    assert np.allclose(s,s_)
    assert len(n.c) ==2 
    assert n.x==1
    assert n.v==None
    assert n.p==None
    assert n.m==None

    for c in n.c:
        assert type(c)==MMNode
        assert c.p==n
        assert c.v==None
        assert len(c.c)==1
    #-----------------------
    # child node A
    s=np.array([[ 1, 1, 1, 1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,0)
            assert x.x==1 # there is no valid move for O player, so O player needs to give up the chance
            ca=x
    assert c

    #-----------------------
    # child node B
    s=np.array([[ 0,-1, 1, 1, 1, 1, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,5)
            assert x.x==-1
            cb=x
    assert c

    #-----------------------
    # Child Node A's children
    # grand child node A1
    assert ca.c[0].p==ca
    assert ca.c[0].v==None
    assert ca.c[0].m==(0,5)
    assert ca.c[0].c==[]
    s=np.array([[ 1, 1, 1, 1, 1, 1, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    assert np.allclose(ca.c[0].s,s)

    #-----------------------
    # Child Node B's children
    # grand child node B1
    assert cb.c[0].p==cb
    assert cb.c[0].v==None
    assert cb.c[0].m==(0,6)
    assert cb.c[0].c==[]
    s=np.array([[ 0,-1,-1,-1,-1,-1,-1, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    assert np.allclose(cb.c[0].s,s)



#-------------------------------------------------------------------------
def test_compute_v():
    '''(5 points) compute_v()'''
    #---------------------
    # Game: TicTacToe
    g = TicTacToe()  # game 

    #-------------------------
    # the value of a terminal node is its game result
    s=np.array([[ 1, 0, 0],
                [ 0, 1,-1],
                [ 0,-1, 1]])
    n = MMNode(s, x=-1)
    n.compute_v(g) 
    assert  n.v== 1 # X player won the game

    # the value of a terminal node is its game result
    s=np.array([[ 1, 1,-1],
                [-1, 1, 1],
                [ 1,-1,-1]])
    n = MMNode(s, x=-1)
    n.compute_v(g) 
    assert  n.v== 0 # A tie 

    # the value of a terminal node is its game result
    s=np.array([[ 1, 0, 1],
                [ 0, 0, 1],
                [-1,-1,-1]])
    n = MMNode(s, x= 1)
    n.compute_v(g) 
    assert  n.v==-1 # O player won the game

    #-------------------------
    # if it is X player's turn, the value of the current node is the max value of all its children nodes.

    s=np.array([[ 0,-1, 1],
                [ 0, 1,-1],
                [ 0,-1, 1]])
    n = MMNode(s, x=1)
    n.build_tree(g)
    # the current node has 3 children nodes, two of which are terminal nodes (X player wins)
    n.compute_v(g) 
    # so the max value among the three children nodes max(1,?,1) = 1 (here ? is either 1 or 0 or -1)
    assert  n.v== 1 # X player won the game

    #-------------------------
    # if it is O player's turn, the value of the current node is the min value of all its children nodes.

    s=np.array([[ 0, 1,-1],
                [ 0,-1, 1],
                [ 1, 1,-1]])
    n = MMNode(s, x=-1)
    n.build_tree(g)
    # the current node has 2 children nodes, one of them is a terminal node (O player wins)
    n.compute_v(g) 
    # so the min value among the two children nodes min(-1,0) =-1 
    assert  n.v==-1 # O player won the game


    #-------------------------
    # a tie after one move
    s=np.array([[-1, 1,-1],
                [-1, 1, 1],
                [ 0,-1, 1]])
    n = MMNode(s, x= 1)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 0  


    #-------------------------
    # optimal moves lead to: O player wins
    s=np.array([[-1, 1,-1],
                [ 1, 0, 0],
                [ 1, 0, 0]])
    n = MMNode(s, x=-1)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v==-1

    #-------------------------
    # optimal moves lead to a tie
    s=np.array([[ 0, 1, 0],
                [ 0, 1, 0],
                [ 0, 0,-1]])
    n = MMNode(s, x=-1)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 0

    #-------------------------
    # optimal moves lead to: X player wins
    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0,-1, 0]])
    n = MMNode(s, x=1)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 1

    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 0,-1]])
    n = MMNode(s, x=1)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 1

    s=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 0, 0]])
    n = MMNode(s, x=1)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 1

    s=np.array([[ 1,-1, 1],
                [-1, 0, 0],
                [ 0, 0, 0]])
    n = MMNode(s, x=1)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 1

    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [-1, 0, 0]])
    n = MMNode(s, x=1)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 1


    s=np.array([[ 1,-1, 1],
                [ 0, 0, 1],
                [ 0, 0,-1]])
    n = MMNode(s, x=-1)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v==-1

    s=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 1,-1]])
    n = MMNode(s, x=1)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 1

    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 1,-1]])
    n = MMNode(s, x=-1)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 0

    # The AI agent should be compatible with both games: TicTacToe and Othello.
    # now let's test on the game "Othello":

    #---------------------
    # Game: Othello 
    g = Othello()  # game 
    s=np.array([[ 0,-1, 1,-1, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    s_ = s.copy()
    n = MMNode(s, x=1) # it's X player's turn
    n.build_tree(g)
    n.compute_v(g)
    assert np.allclose(s,s_)
    assert  n.v== 1
    
    s=np.array([[ 0, 0,-1, 1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    n = MMNode(s, x=1) # it's X player's turn
    n.build_tree(g)
    n.compute_v(g)
    assert  n.v==-1
    

    s=np.array([[ 0, 0,-1, 1, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    n = MMNode(s, x=-1) # it's O player's turn
    n.build_tree(g)
    n.compute_v(g)
    assert  n.v==-1
    n = MMNode(s, x=1) # it's X player's turn
    n.build_tree(g)
    n.compute_v(g)
    assert  n.v==1


    s=np.array([[ 0,-1, 1,-1, 1,-1, 0, 0],
                [ 1, 0, 0, 0, 0, 0, 0, 0],
                [ 1, 0, 0, 0, 0, 0, 0, 0],
                [-1, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    n = MMNode(s, x=1) # it's X player's turn
    n.build_tree(g)
    n.compute_v(g)
    assert  n.v==1


#-------------------------------------------------------------------------
def test_choose_optimal_move():
    '''(5 points) choose_optimal_move()'''
    #---------------------
    # Game: TicTacToe
    g = TicTacToe()  # game 
    p = MiniMaxPlayer()

    #-------------------------
    s=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 1,-1]])
    n = MMNode(s, x=1)
    n.build_tree(g)
    n.compute_v(g) 
    r,c=p.choose_optimal_move(n)
    assert r == 2
    assert c == 0

    #-------------------------
    s=np.array([[ 1,-1, 1],
                [ 0, 1,-1],
                [ 0, 1,-1]])
    n = MMNode(s, x=-1)
    n.build_tree(g)
    n.compute_v(g) 
    r,c=p.choose_optimal_move(n)
    assert r == 2
    assert c == 0

    #-------------------------
    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 0, 0]])
    n = MMNode(s, x=-1)
    n.build_tree(g)
    n.compute_v(g) 
    r,c=p.choose_optimal_move(n)
    assert r == 1
    assert c == 1

    #-------------------------
    s=np.array([[ 1,-1, 1],
                [ 0, 1,-1],
                [-1, 1,-1]])
    n = MMNode(s, x=1)
    n.build_tree(g)
    n.compute_v(g) 
    r,c=p.choose_optimal_move(n)
    assert r == 1
    assert c == 0


    # The AI agent should be compatible with both games: TicTacToe and Othello.
    # now let's test on the game "Othello":

    #---------------------
    # Game: Othello 
    g = Othello()  # game 
    s=np.array([[ 0,-1, 1,-1, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    s_ = s.copy()
    n = MMNode(s, x=1) # it's X player's turn
    n.build_tree(g)
    n.compute_v(g)
    assert np.allclose(s,s_)
    r,c=p.choose_optimal_move(n)
    assert r == 0
    assert c == 0


#-------------------------------------------------------------------------
def test_minmax_choose_a_move():
    '''(10 points) minmax choose_a_move()'''

    #---------------------
    # Game: TicTacToe
    g = TicTacToe()  # game 

    # two possible moves: one leads to win
    p = MiniMaxPlayer()
    s=np.array([[ 0,-1, 1],
                [-1, 1, 1],
                [ 0, 1,-1]])
    s_ = s.copy()
    r, c = p.choose_a_move(g,s,x=1)
    assert np.allclose(s,s_)
    assert r==2  
    assert c==0  


    # three possible moves, one leads to win
    p = MiniMaxPlayer()
    s=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 1,-1]])

    r, c = p.choose_a_move(g,s,x=1) 
    assert r==2  
    assert c==0  

    #-------------------------
    p = MiniMaxPlayer()
    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 0, 0]])
    r, c = p.choose_a_move(g,s,x=-1) # O player's turn
    assert r == 1
    assert c == 1


    #-------------------------
    # play against random player in the game
    p1 = MiniMaxPlayer()
    p2 = RandomPlayer()

    # X Player: MinMax
    # O Player: Random 
    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 0,-1]])
    for i in range(10):
        e = g.run_a_game(p1,p2,s=s,x=1)
        assert e==1


    #-------------------------
    # play against MinMax player in the game

    # X Player: MinMax 
    # O Player: MinMax  
    s=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 1,-1]])
    for i in range(10):
        e = g.run_a_game(p1,p1,s=s,x=1)
        assert e==1

    s=np.array([[ 0, 0, 1],
                [ 0,-1, 0],
                [ 1,-1, 0]])
    e = g.run_a_game(p1,p1,s=s)
    assert e==0

    s=np.array([[ 0, 0, 0],
                [ 0,-1, 0],
                [ 1, 0, 0]])
    e = g.run_a_game(p1,p1,s=s)
    assert e==0

    s=np.array([[ 0, 0, 0],
                [ 0, 0, 0],
                [ 1,-1, 0]])
    e = g.run_a_game(p1,p1,s=s)
    assert e==1

    s=np.array([[ 0, 0, 0],
                [ 0, 1, 0],
                [ 0,-1, 0]])
    e = g.run_a_game(p1,p1,s)
    assert e==1

    s=np.array([[ 0, 0, 0],
                [ 0, 1, 0],
                [-1, 0, 0]])
    e = g.run_a_game(p1,p1,s)
    assert e==0

    #******************************************************
    #*******************(TRY ME)***************************
    #******************************************************
    '''Run A Complete Game (TicTacToe): 
       the following code will run a complete TicTacToe game using MiniMaxPlayer,     
       if you want to try this, uncomment the following three lines of code.
       Note: it may take 1 or 2 minutes to run
    '''
    #g = TicTacToe()
    #e = g.run_a_game(p1,p1)
    #assert e==0
    #******************************************************
    #******************************************************
    #******************************************************



    #----------------------------------------------
    # The AI agent should be compatible with both games: TicTacToe and Othello.
    # now let's test on the game "Othello":

    #---------------------
    # Game: Othello 
    g = Othello()  # game 
    s=np.array([[ 0,-1, 1,-1, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    for i in range(10):
        e = g.run_a_game(p1,p2,s=s,x=1)
        assert e==1

    w=0
    for i in range(10):
        e = g.run_a_game(p2,p2,s=s,x=1)
        w+=e 
    assert np.abs(w)<9



    #******************************************************
    #*******************(DO NOT TRY ME:)*******************
    #******************************************************
    ''' Run A Complete Game (Othello): 
        The following code will run a complete Othello game using MiniMaxPlayer,     
        If you want to try this, uncomment the following two lines of code. 
        My suggestion: Don't let it run for a long time, stop the program in the terminal after 1 or 2 minutes.
        Otherwise it will eventually use up all your computer's memory. Even with unlimited memory, your computer will still need to run forever to build the search tree! So spending 1 or 2 minutes on this program should be enough to prove that there is no hope for MiniMax method on large board games. 
    '''
    #g = Othello()
    #e = g.run_a_game(p1,p1)
    #******************************************************
    #******************************************************
    #******************************************************

