import random
WIDTH = 21
HEIGHT = 21

DIRS = [(-2, 0), (2, 0), (0, -2), (0, 2)]

def init_maze(width, height):
    return [[1 for _ in range(width)] for _ in range(height)]

def in_bounds(x, y, width, height):
    return 0 <= x < height and 0 <= y < width

def generate_maze(maze, x, y):
    maze[x][y] = 0
    random.shuffle(DIRS)
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        mx, my = x + dx // 2, y + dy // 2
        if in_bounds(nx, ny, WIDTH, HEIGHT) and maze[nx][ny] == 1:
            maze[mx][my] = 0
            generate_maze(maze, nx, ny)

# Solve the maze using DFS
def solve_maze(maze, start, end):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (x, y), path = stack.pop()
        if (x, y) == end:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in DIRS:
            nx, ny = x + dx // 2, y + dy // 2
            if in_bounds(nx, ny, WIDTH, HEIGHT) and maze[nx][ny] == 0:
                stack.append(((nx, ny), path + [(nx, ny)]))
    return None


def print_maze(maze, path=None, save=False):
    output = ""
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) == (1, 1):
                output += 'S'
            elif (i, j) == (HEIGHT - 2, WIDTH - 2):
                output += 'E'
            elif path and (i, j) in path:
                output += '.'
            elif maze[i][j] == 1:
                output += '█'
            else:
                output += ' '
        output += '\n'
    print(output)
    

    if save:
        with open("output.txt", "w", encoding="utf-8") as f:
          f.write(output)
        print("✅ Maze saved to 'output.txt'")


maze = init_maze(WIDTH, HEIGHT)
generate_maze(maze, 1, 1)
start = (1, 1)
end = (HEIGHT - 2, WIDTH - 2)
path = solve_maze(maze, start, end)

print_maze(maze, path, save=True)