def assembly_line(a, t, e, x, n):
    line1 = e[0] + a[0][0]
    line2 = e[1] + a[1][0]

    for i in range(1, n):

        # Line 1
        new_line1 = min(
            line1 + a[0][i],
            line2 + t[1][i - 1] + a[0][i]
        )

        # Line 2
        new_line2 = min(
            line2 + a[1][i],
            line1 + t[0][i - 1] + a[1][i]
        )

        line1 = new_line1
        line2 = new_line2

    # Add exit time
    return min(line1 + x[0], line2 + x[1])


# Processing time at each station
a = [
    [4, 5, 3, 2],
    [2, 10, 1, 4]
]

# Transfer time
t = [
    [0, 7, 4, 5],
    [0, 9, 2, 8]
]

# Entry time
e = [10, 12]

# Exit time
x = [18, 7]

n = 4

result = assembly_line(a, t, e, x, n)

print("Minimum time:", result)