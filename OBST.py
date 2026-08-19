def optimal_bst(keys, freq):
    n = len(keys)

    dp = [[0] * n for _ in range(n)]

    # Cost of a single key
    for i in range(n):
        dp[i][i] = freq[i]

    # Chain length
    for length in range(2, n + 1):

        for i in range(n - length + 1):

            j = i + length - 1

            dp[i][j] = float('inf')

            total_freq = sum(freq[i:j + 1])

            for r in range(i, j + 1):

                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0

                cost = left + right + total_freq

                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


keys = [10, 12, 20]
freq = [34, 8, 50]

result = optimal_bst(keys, freq)

print("Minimum Cost:", result)