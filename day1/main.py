from __future__ import print_function

test1Data = [[1,1,1,1,0],
             [1,1,0,1,0],
             [1,1,0,0,0],
             [0,0,0,0,0]]

test2Data = [[1,1,0,0,0],
             [1,1,0,0,0],
             [0,0,1,0,0],
             [0,0,0,1,1]]

tests = [test1Data, test2Data]

def union(parents,x,y):
    """
    Joins set x and y together by making set y the 
    representative node of set x
    """
    xset = find_root(parents,x)
    yset = find_root(parents,y)
    parents[xset] = yset

def find_root(parents,idx):
    """
    Finds the representative node of a given element
    """
    if parents[idx] != idx:
        parents[idx] = find_root(parents,parents[idx])
    return parents[idx]

def is_valid(x,y,n,m):
    """
    checks if the x,y position is valid in an NxM matrix
    """
    if x < 0 or x >= n: return False
    if y < 0 or y >= m: return False
    return True

def get_num_components(data):
    """
    Calculates the number of connected components in a 2d graph.
    connectedness is defined as adjaceny left, right, top bottom
    """
    #make everything a set by itself, set all 0 to the same set
    n = len(data)           #number of rows
    m = len(data[0])        #number of columns
    parents = [-1] * (n*m) 
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                parents[i*m + j] = -1
            else:
                parents[i*m + j] = i*m + j
    
    #for each node, run union find on top,bottom,left,right
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if is_valid(ni,nj,n,m) and data[ni][nj] == 1:
                        union(parents,i*m + j, ni*m + nj)
    for i in range(n*m):
        if parents[i] == -1: continue
        parents[i] = find_root(parents,i)
    #print(parents)

    components = set(parents)
    components.remove(-1)     #skip counting the -1 components
    return len(components)

#Test Driver
for i,test in enumerate(tests):
    components = get_num_components(test)
    print('{} components in test data {}'.format(components,i))
