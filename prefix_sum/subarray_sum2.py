#METHOD 1:

# sort the array,
# maintain a window: i,j. If the difference between the first and last element is 1.
#   keep increasing 1 and thus length of max substring. 


def sort_method(arr)->int:
    sorted_arr = sorted(arr)
    j = 0
    max_len = 0
    for i in range(len(sorted_arr)):
        while sorted_arr[i]-sorted_arr[j] > 1:
            j+=1
        if sorted_arr[i]-sorted_arr[j]==1:
            max_len = max(max_len,i-j+1)
    return max_len

def hashmap_method(arr):
    freq_map = {}
    for ele in arr:
        freq_map[ele] = freq_map.get(ele,0)+1
    max_len = 0
    for ele, freq in freq_map.items():
        if ele+1  in freq_map:
            max_len = max(max_len,freq+freq_map[ele+1])
    return max_len

arr = [1,3,2,2,5,2,3,7]

print(sort_method(arr))
print(hashmap_method(arr))