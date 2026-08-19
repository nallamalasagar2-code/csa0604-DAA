def median_of_medians(arr, k):

    # If array has 5 or fewer elements
    if len(arr) <= 5:
        arr.sort()
        return arr[k - 1]

    # Divide array into groups of 5
    groups = []

    for i in range(0, len(arr), 5):
        group = arr[i:i + 5]
        group.sort()
        groups.append(group)

    # Find median of each group
    medians = []

    for group in groups:
        median = group[len(group) // 2]
        medians.append(median)

    # Find median of medians
    pivot = median_of_medians(medians, (len(medians) + 1) // 2)

    # Divide elements around pivot
    smaller = []
    equal = []
    larger = []

    for x in arr:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    # Find kth smallest
    if k <= len(smaller):
        return median_of_medians(smaller, k)

    elif k <= len(smaller) + len(equal):
        return pivot

    else:
        new_k = k - len(smaller) - len(equal)
        return median_of_medians(larger, new_k)


# Main program
arr = [12, 3, 5, 7, 4, 19, 26, 8, 15, 2, 10]
k = 5

result = median_of_medians(arr, k)

print("Array:", arr)
print("K =", k)
print("Kth smallest element:", result)