import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
# 15,5 64,83
# 0 = Empty
# 1 = Wall
# 2 = Start
# 3 = End
# 4 = Queued
# 5 = Visited
# 6 = Found Path

def BFS(maze, s):
    queue = [s]         # Queue the start
    maze[s[0],s[1]] = 4 

    depthCounter = 0    # number of nodes checked

    modifiedNodes = []  # Used in plotting
    modifiedNodeStatus = []
    pathEdges = {}
    while queue != []:
        depthCounter += 1
        currNode = queue.pop(0) # FIFO queue
        
        # Check surrounding 8 (or 4) nodes
        #for i in [-1,0,1]:
            #for j in [-1,0,1]:
                #adjNode = currNode + [i,j]
        for i in [[0,-1],[0,1],[-1,0],[1,0]]:    
            adjNode = currNode + i
            
            # end node: quit
            if maze[adjNode[0],adjNode[1]] == 3:    
                queue = []
                pathEdges[tuple([adjNode[0],adjNode[1]])] = tuple([currNode[0],currNode[1]])
                break    
            # open node: add to queue                           
            elif maze[adjNode[0],adjNode[1]] == 0:    
                maze[adjNode[0],adjNode[1]] = 4     
                queue.append(adjNode)
                pathEdges[tuple([adjNode[0],adjNode[1]])] = tuple([currNode[0],currNode[1]])
  
                modifiedNodes.append([adjNode[0],adjNode[1]])   # Plotting stuff
                modifiedNodeStatus.append(4)

        maze[currNode[0],currNode[1]] = 5   # mark current as Visitied
        modifiedNodes.append([currNode[0],currNode[1]]) # Plotting stuff
        modifiedNodeStatus.append(5)
                
        if depthCounter%100 == 0:
            Plot_Search_Path(modifiedNodes, modifiedNodeStatus)
            modifiedNodes = []
            modifiedNodeStatus = []

    Plot_Search_Path(modifiedNodes, modifiedNodeStatus)

    shortestPath = [tuple([adjNode[0],adjNode[1]])]
    while True:
        if shortestPath[-1] in pathEdges:
            shortestPath.append(pathEdges[shortestPath[-1]])
        else:
            break

    return shortestPath

def Draw_Maze_Innit(mazelist):
    # Loop over all points in maze
    rowCounter = 0
    entryCounter = 0
    for row in mazelist:
        for entry in row:       
            # Plotting maze outline and POI
            if entry == 1:      # Obstacle
                ax.plot(entryCounter, rowCounter, 'k.')
            elif entry == 2:    # Start
                ax.plot(entryCounter, rowCounter, 'bo')
            elif entry == 3:    # End
                ax.plot(entryCounter, rowCounter, 'go')
            elif entry == 4:    # Queued
                ax.plot(entryCounter, rowCounter, 'mx')
            elif entry == 5:    # Visited
                ax.plot(entryCounter, rowCounter, 'c.')
            entryCounter += 1
        rowCounter += 1
        entryCounter = 0
    ax.axis('equal')
    plt.pause(1e-10)
    return

def Plot_Search_Path(points, stati):    
    for nodeNum in range(len(points)):
        if stati[nodeNum] == 4:    # Queued
            color = 'mx'
        elif stati[nodeNum] == 5:    # Visited
            color = 'cx'

        ax.plot(points[nodeNum][1],points[nodeNum][0],color)
    plt.pause(1e-10)
    return

def PlotPath(path):
    xcoords = []
    ycoords = []
    for node in path:
        ycoords.append(node[0])
        xcoords.append(node[1])

    plt.plot(xcoords,ycoords,'r-')
    return


if __name__ == '__main__':
    mazeList = pd.read_csv("Homework 1\Map3.csv", header=None).to_numpy()
    
    height, width = mazeList.shape
    start = np.where(mazeList==2)
    startLoc = np.array([start[0][0],start[1][0]])

    # Start interactive plot
    plt.ion()
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111)

    Draw_Maze_Innit(mazeList)
    shortestPath = BFS(mazeList, startLoc)
    PlotPath(shortestPath)

    # Keeping the updating plot open
    while True:
        plt.pause(10)