#Formula P[i][j] = P[i][j-1] + P[i-1][j]  - P[i-1][j-1] + A[i][j]

n,m = map(int, input("Enter number of rows and columns: ").split())

v = []
for i in range(n):
    v.append([0]*m)

for i in range(n):
    print(f"Enter values for row {i}")
    for j in range(m):
        v[i][j] = int(input(f"Value for cell {i}-{j}: "))
    print()

pre = []
for i in range(n):
    pre.append([0]*m)

for i in range(n):
    for i in range(m):
        
        pre[i][j] =  v[i][j]
        if j>0:
            pre[i][j]+= pre[i][j-1]
        if i>0:
            pre[i][j]+= pre[i-1][j]
        if i>0 and j>0:
            pre[i][j]+= pre[i-1][j-1]


q = int(input("Number of queries: "))

for i in range(q):
    i1,j1,i2,j2 = map(int,input("Enter the two end  points of the rectangle").split())
    ans = pre[i2][j2]

    if i1>0:
        ans -=pre[i1-1][j2]
    if j1> 0:
        ans -=pre[i2][j1-1]
    if i1>0 and j1>0:
        ans +=pre[i1-1][j1-1]

    print(ans)    

    