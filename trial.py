#Formula P[i][j] = P[i][j-1] + P[i-1][j]  - P[i-1][j-1] + A[i][j]


matrix = [
    [1,2,3,5,6],
    [3,6,7,7,2],
    [1,3,5,6,7],
    [1,3,5,6,6]
]

m = len(matrix[0])
n = len(matrix)

# calculate prefix sum

prefix_sum = []

for i in range(n):
    prefix_sum.append([0]*m)



for i in range(n):
    for j in range(m):
        pre_sum = matrix[i][j]

        if i-1>=0:
            pre_sum += prefix_sum[i-1][j]
        if j-1>=0:
            pre_sum += prefix_sum[i][j-1]

        if i-1>=0 and j-1>=0:
            pre_sum -= prefix_sum[i-1][j-1]
        prefix_sum [i][j] = pre_sum

for i in range(n):
    for j in range(m):
        print(prefix_sum[i][j],end =" ")
    print()