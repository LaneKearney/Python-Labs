from Stack import Stack

def maze_path_exists(maze, start_x, start_y):  
    s = Stack()
    s.push([start_x, start_y])
    count = 1
    maze[start_x][start_y] = count
    while not s.isEmpty():
        currentPosition = s.peek()
        x, y = currentPosition[0], currentPosition[1]


        if x - 1 >= 0 and maze[x - 1][y] == 'G':
            return True
        if x - 1 >= 0 and maze[x - 1][y] == ' ':
            count += 1
            maze[x - 1][y] = count
            s.push([x - 1,y])
            continue

        if  y - 1 >= 0 and maze[x][y - 1] == 'G':
            return True
        if y - 1 >= 0 and maze[x][y - 1] == ' ':
            count += 1
            maze[x][y - 1] = count
            s.push([x,y - 1])
            continue

        if x + 1 < len(maze[0]) and maze[x + 1][y] == 'G':
            return True
        if x + 1 < len(maze[0]) and maze[x + 1][y] == ' ':
            count += 1
            maze[x + 1][y] = count
            s.push([x + 1,y])
            continue

        if y + 1 < len(maze[0]) and maze[x][y + 1] == 'G':
            return True
        if y + 1 < len(maze[0]) and maze[x][y + 1] == ' ':
            count += 1
            maze[x][y + 1] = count
            s.push([x,y + 1])
            continue
        s.pop()

    return False