"""
Given a Square matrix N x N,
find sum of the elem in the main diagonal 
Input:
First line N - size of matrix
second line N - space separated integers

3
123
456
789

Output:
15
"""

def find_trace(matrix):
    n = len(matrix)

    trace = sum(matrix[i][i] for i in range(n))
    """
    Iteration 1 (i=0): It accesses matrix[0][0] (the top-left corner: 1).
    Iteration 2 (i=1): It accesses matrix[1][1] (the center: 5).
    Iteration 3 (i=2): It accesses matrix[2][2] (the bottom-right: 9).

    """
    return trace

n = int(input("Enter the size of matrix: "))
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print(find_trace(matrix))
