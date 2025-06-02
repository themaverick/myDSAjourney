def ratMaze(srcx, srcy, maze, m, n, vis, ans, str1):
    if srcx >= len(maze) or srcx < 0 or srcy >= len(maze[0]) or srcy < 0 or maze[srcx][srcy] == 0 or vis[srcx][srcy] == 1:
        return
    
    if srcx == m and srcy == n:
        ans.append("".join(str1))
        return
    
    vis[srcx][srcy] = 1

    str1.append("D")
    ratMaze(srcx+1, srcy, maze, m, n, vis, ans, str1)
    str1.pop()

    str1.append("U")
    ratMaze(srcx-1, srcy, maze, m, n, vis, ans, str1)
    str1.pop()

    str1.append("R")
    ratMaze(srcx, srcy+1, maze, m, n, vis, ans, str1)
    str1.pop()

    str1.append("L")
    ratMaze(srcx, srcy-1, maze, m, n, vis, ans, str1)
    str1.pop()
    vis[srcx][srcy] = 0


srcx = 1
srcy = 0
maze = [[1, 0, 0, 0], 
        [1, 1, 0, 0], 
        [0, 1, 1, 0], 
        [0, 0, 1, 1]]
vis =  [[0]*len(maze[0]) for _ in range(len(maze))]

for i in range(len(vis)):
    for j in range(len(vis[0])):
        vis[i][j] = 0
m = 3
n = 3
ans = []
str1 = []
ratMaze(srcx, srcy, maze, m, n, vis, ans, str1)
print(ans)
