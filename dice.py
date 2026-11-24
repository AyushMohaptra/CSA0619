def dice_throwing(n, faces, target):
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for dice in range(1, n + 1):
        for total in range(1, target + 1):
            dp[dice][total] = sum(
                dp[dice - 1][total - face]
                for face in range(1, min(faces, total) + 1)
            )
    return dp[n][target]
