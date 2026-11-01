def karatsuba(x, y):
  if x < 10 or y < 10:
    return x * y
  m = max(len(str(x)), len(str(y))) // 2
  high1, low1 = divmod(x, 10**m)
  high2, low2 = divmod(y, 10**m)
  z0, z2 = karatsuba(low1, low2), karatsuba(high1, high2)
  z1 = karatsuba(low1 + high1, low2 + high2) - z0 - z2
  return z2 * 10 ** (2 * m) + z1 * 10**m + z0
