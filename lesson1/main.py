def find_min(arr):
    min = arr[0]
    n = len(arr)
    for i in range(0, n):
        if arr[i] <min:
            min = arr[i]
    return min

a = [325, 123, 21, 52, 789, 2, 32]
m = find_min(a)
print(m)
















































































