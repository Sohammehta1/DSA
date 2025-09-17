def number_of_subarrays(arr, target):
    prefix_map = {0:1}  # Prefix sum 0 is seen once
    running_sum = 0
    res = 0

    for num in arr:
        running_sum += num
        res += prefix_map.get(running_sum - target,0)
        prefix_map[running_sum] = prefix_map.get(running_sum, 0) + 1

    return res

# arr= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# target = 0

size, target = map(int, input().split())

arr = [int(num) for num in input().split()]

print(number_of_subarrays(arr,target))