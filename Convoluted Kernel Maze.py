#!/usr/bin/env python
# coding: utf-8

# In[2]:


from random import randint


# In[3]:


def build_maze(m,n,swag):
    grid = []
    grid = [['wall' for col in range(n)] for row in range(m)]
    start_i, start_j = randint(0,m-1), randint(0,n-1)
    grid[start_i][start_j] = 'start'
    mow(grid,start_i,start_j)
    explore_maze(grid, start_i, start_j, swag)
    return grid


# In[4]:


def print_maze(grid):
    for row in grid:
        printable_row = ''
        for cell in row:
            if cell == 'wall':
                char = '|'
            elif cell == 'start':
                char = 'X'
            elif cell == 'empty':
                char = ' '
            else:
                char = cell[0]
            printable_row += char
        print(printable_row)


# In[5]:


def mow(grid, i, j):
    directions = ['U', 'D', 'L', 'R']
    while len(directions) > 0:
        directions_index = randint(0,len(directions)-1)
        direction = directions.pop(directions_index)
        if direction == 'U':
            if i - 2 < 0:
                continue
            elif grid[i - 2][j] == 'wall':
                grid[i - 1][j] = 'empty'
                grid[i - 2][j] = 'empty'
                mow(grid, i - 2, j)
        elif direction == 'D':
            if i + 2 >= len(grid):
                continue
            elif grid[i + 2][j] == 'wall':
                grid[i + 1][j] = 'empty'
                grid[i + 2][j] = 'empty'
                mow(grid, i + 2, j)
        elif direction == 'L':
            if j - 2 < 0:
                continue
            elif grid[i][j-2] == 'wall':
                grid[i][j-1] = 'empty'
                grid[i][j-2] = 'empty'
                mow(grid, i, j - 2)
        else:
            if j + 2 >= len(grid[0]):
                continue
            elif grid[i][j+2] == 'wall':
                grid[i][j+1] = 'empty'
                grid[i][j+2] = 'empty'
                mow(grid, i, j+2)


# In[8]:


def explore_maze(grid, start_i, start_j, swag):
    grid_copy = [row[:] for row in grid]
    bfs_queue = [[start_i, start_j]]
    directions = ['U','D', 'L', 'R']
  
    while bfs_queue:
        i, j = bfs_queue.pop(0)
        if grid[i][j] != 'start' and randint(1,10) == 1:
            grid[i][j] = swag[randint(0, len(swag) - 1)]
        grid_copy[i][j] = 'visited'
        
        for direction in directions:
            explore_i, explore_j = i, j
            if direction == 'U':
                explore_i = i - 1
            elif direction == 'D':
                explore_i = i + 1
            elif direction == 'L':
                explore_j = j - 1
            else:
                explore_j = j + 1
            if explore_i < 0 or explore_j < 0 or explore_i >= len(grid) or explore_j >= len(grid[0]):
                continue
        
            elif grid_copy[explore_i][explore_j] != 'visited' and grid_copy[explore_i][explore_j] != 'wall':
                bfs_queue.append([explore_i, explore_j])
    grid[i][j] = 'end'


# In[12]:


print_maze(build_maze(15,25,['candy corn', 'werewolf', 'pumpkin']))


# In[ ]:


#print_maze(build_maze(5,10,None))

