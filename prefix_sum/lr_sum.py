#For every query l,r calculate sum like: A[l] + 2*A[l+1].....+(r-l+1)*A[r]
# basically sum: from i=r->l Ai(i-L+1)

def calculate_rl_sum(arr,l,r):
    n = len(arr)
    index_arr = []
    prefix_arr  = []
    s=0
    for i,ele in enumerate(arr):
        s += ele
        prefix_arr.append(s)
        index_arr.append(s+ ele*i)

    index_prefix_sum = index_arr[r]
    if l>0:
        index_prefix_sum-=index_arr[l-1]

    prefix_sum = prefix_arr[r]
    if l>0:
        prefix_arr-=prefix_arr[l-1]
    
    return index_prefix_sum - prefix_sum*(l-1)

