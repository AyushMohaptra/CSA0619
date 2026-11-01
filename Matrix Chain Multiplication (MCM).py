def mcm(p):
  n = len(p)
  dp = [[0] * n for _ in range(n)]
  for L in range(2, n):
    for i in range(1, n - L + 1):
      j = i + L - 1
      dp[i][j] = min(
          dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
          for k in range(i, j)
      )
  return dp[1][n - 1]
