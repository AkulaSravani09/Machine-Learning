matrix = [
    [1, 0],
    [0, 2]
]
snake_x, snake_y = 0, 0

new_x = snake_x
new_y = snake_y + 1

if matrix[new_x][new_y] == 2:
    print("Food eaten")

matrix[snake_x][snake_y] = 0
matrix[new_x][new_y] = 1

for row in matrix:
    print(row)