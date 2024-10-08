import numpy as np
#-------------------------------------------------------------------------
'''
    Problem 3: PageRank algorithm (version 1) 
    In this problem, we implement a simplified version of the pagerank algorithm, which doesn't consider sink node problem or sink region problem.
    
    How to run the unit tests to test your code?
    1) Test one function in a test file:
       After implementing one function in this file (for example, compute_P), you could test the correctness of your code by typing `nosetests -v test3.py:test_compute_P' in the terminal.
    2) Test all functions in one test file:
       After solving all the functions in a test file (for example, test3.py), you could test the correctness of your code by typing `nosetests -v test3.py' in the terminal.
'''

#--------------------------
def compute_P(A):
    '''
        compute the transition matrix P from adjacency matrix A. P[j][i] represents the probability of moving from node i to node j.
        Input: 
                A: adjacency matrix, a (n by n) numpy matrix of binary values. If there is a link from node i to node j, A[j][i] =1. Otherwise A[j][i]=0 if there is no link.
        Output: 
                P: transition matrix, a (n by n) numpy matrix of float values.  P[j][i] represents the probability of moving from node i to node j.
                   The values in each column of matrix P should sum to 1.
        Hint: you could solve this problem using 3 lines of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE

    # indicies with 1 are replaced with 1/(sum of column)

    P = A / A.sum(axis=0)

    #########################################
    return P


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_compute_P' in the terminal.  '''




#--------------------------
def random_walk_one_step(P, x_i):
    '''
        compute the result of one step random walk.
        Input: 
                P: transition matrix, a (n by n) numpy matrix of float values.  P[j][i] represents the probability of moving from node i to node j.
                x_i: pagerank scores before the i-th step of random walk. a numpy vector of length n.
        Output: 
                x_i_plus_1: pagerank scores after the i-th step of random walk. a numpy vector of length n.
        Hint: you could solve this problem using one line of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE

    x_i_plus_1 = P.dot(x_i)

    #########################################
    return x_i_plus_1

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_random_walk_one_step' in the terminal.  '''


#--------------------------
def random_walk(P, x_0, max_steps=10000):
    '''
        Compute the result of multiple-step random walk. 
        The random walk should stop if the score vector x no longer change (converge) after one step of random walk, or the number of iteration reached max_steps.
        Input: 
                P: transition matrix, a (n by n) numpy matrix of float values.  P[j][i] represents the probability of moving from node i to node j.
                x_0: the initial pagerank scores. a numpy vector of length n.
                max_steps: the maximum number of random walk steps. an integer value.  
        Output: 
                x: the final pagerank scores after multiple steps of random walk. a numpy vector of length n.
                n_steps: the number of steps of random walk actually used (for example, if the vector x no longer changes after 3 steps of random walk, return the value 3. 
        Hint: You could re-use the previous function (random_walk_one_step) to simulate the random walk in each step.
              You could use np.allclose(previous_x, new_x) function to determine when to stop the random walk iterations.
              If the value of x in the previous iteration (previous_x) is close enough to the new value of x (new_x), the stop the iteration and return the latest value of x.
    '''
    #########################################
    ## INSERT YOUR CODE HERE

    x, n_steps = x_0, 0
    for i in range(0, max_steps):
        old = x
        x = P.dot(x)
        n_steps += 1
        if np.allclose(x, old):
            break

    #########################################
    return x, n_steps

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_random_walk' in the terminal.  '''



#--------------------------
def pagerank_v1(A):
    ''' 
        A simplified version of PageRank algorithm.
        Given an adjacency matrix A, compute the pagerank score of all the nodes in the network. 
        Here we ignore the issues of sink nodes and sink regions in the network.
        Input: 
                A: adjacency matrix, a numpy matrix of binary values. If there is a link from node i to node j, A[j][i] =1. Otherwise A[j][i]=0 if there is no link.
        Output: 
                x: the pagerank scores, a numpy vector of float values, such as np.array([.3, .2, .5])
        Hint: you could solve this problem using two lines of code. Re-use the previous functions that you have implemented to solve this problem.
    '''
    # initialize the pagerank score vector
    num_nodes = A.shape[0] # get the number of nodes (n)
    x_0 =  np.ones(num_nodes)/num_nodes 
    
    #########################################
    ## INSERT YOUR CODE HERE

    # compute the transition matrix P from adjacency matrix A
    P = A / A.sum(axis=0)

    # random walk for multiple steps, until convergence
    x, _ = random_walk(P, x_0)

    #########################################

    return x






#--------------------------------------------

''' TEST ALL: 
        Now you can test the correctness of all the above functions by typing `nosetests -v test3.py' in the terminal.  

        If your code passed all the tests, you will see the following message in the terminal:
                ---------- Problem 3 (30 points in total) ------------ ... ok
                (10 points) compute_P ... ok
                (5 points) random_walk_one_step ... ok
                (10 points) random_walk ... ok
                (5 points) pagerank_v1 ... ok
                
                ----------------------------------------------------------------------
                Ran 5 tests in 0.006s
                
                OK

'''

#--------------------------------------------


