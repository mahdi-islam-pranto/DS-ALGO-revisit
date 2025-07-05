arr = [11, 15, 2, 7]
target = 9
loop_count = 0

# 1 way : O(n^2)

# fist loop (starts from 0)
for i in range(len(arr)):
    # 2nd loop (starts from i+1 )
    for j in range(i+1, len(arr)):
        loop_count += 1
        print(f'{loop_count}:::: index: {i}+{j}')
        if arr[i]+arr[j] == target:
            print(f'Found the target {target} at index {i} and {j}')
            print([i,j])
            break       # break the inner loop
        else: continue
    if arr[i]+arr[j] == target:  
        break    # break the outer loop too
            



nums = [11, 15, 2, 7]
target = 9
loop_count = 0

# 2 way : O(n) using hashmap
hashmap = {}
for i in range(len(nums)):
    if (nums[i]) in hashmap:
        get_index = hashmap[nums[i]]
        print(get_index, i)
        break
    else:
        # add the number to hashmap
        hashmap[target-nums[i]] = i
        print(hashmap)
        