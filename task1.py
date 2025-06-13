def generate_spiral(n):
    
    output_matrix = [[0] * n for i in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1
    direction = 0 
    
    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                output_matrix[top][i] = num
                num += 1
            top += 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                output_matrix[i][right] = num
                num += 1
            right -= 1
        elif direction == 2:
            for i in range(right, left - 1, -1):
                output_matrix[bottom][i] = num
                num += 1
            bottom -=1  
        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                output_matrix[i][left] = num
                num += 1
            left += 1
        direction = (direction + 1) % 4
    return output_matrix
    
    
n = 5
result = generate_spiral(n)

print(f"Generated matrix for n = {n}")
for row in result:
    print(row)
