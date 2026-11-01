def subset_sum(arr, target):
  dp = [True] + [False] * target
  for x in arr:
    for i in range(target, x - 1, -1):
      dp[i] = dp[i] or dp[i - x]
  return dp[target]
