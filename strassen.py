import numpy as np
def strassen(A, B):
  if len(A) <= 1:
    return A * B
  mid = len(A) // 2
  A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
  B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]
  M1 = strassen(A11 + A22, B11 + B22)
  M2 = strassen(A21 + A22, B11)
  M3 = strassen(A11, B12 - B22)
  M4 = strassen(A22, B21 - B11)
  M5 = strassen(A11 + A12, B22)
  M6 = strassen(A21 - A11, B11 + B12)
  M7 = strassen(A12 - A22, B21 + B22)
  return np.vstack((
      np.hstack((M1 + M4 - M5 + M7, M3 + M5)),
      np.hstack((M2 + M4, M1 - M2 + M3 + M6)),
  ))
