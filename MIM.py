def subset_sums(arr):
    n = len(arr)
    result = []

    for mask in range(1 << n):
        total = 0

        for i in range(n):
            if mask & (1 << i):
                total += arr[i]

        result.append(total)

    return result


arr = [2, 4, 6, 8]
target = 10

mid = len(arr) // 2

left = arr[:mid]
right = arr[mid:]

left_sums = subset_sums(left)
right_sums = subset_sums(right)

found = False

for x in left_sums:
    if target - x in right_sums:
        found = True
        break

if found:
    print("Subset with given sum exists")
else:
    print("Subset does not exist")