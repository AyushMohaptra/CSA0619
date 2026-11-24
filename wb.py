def word_break(text, dictionary):
    words = set(dictionary)
    dp = [False] * (len(text) + 1)
    dp[0] = True
    for end in range(1, len(text) + 1):
        dp[end] = any(
            dp[start] and text[start:end] in words
            for start in range(end)
        )
    return dp[-1]

