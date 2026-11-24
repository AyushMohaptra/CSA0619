def text_matching(text, pattern):
    if pattern == "":
        return list(range(len(text) + 1))
    return [
        i for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]
