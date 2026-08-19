def lps(s):
    n = len(s)

    dp = [[0] * n for _ in range(n)]

    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):

        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2

            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


s = "BBABCBCAB"

print("String:", s)
print("Longest Palindromic Subsequence:", lps(s))