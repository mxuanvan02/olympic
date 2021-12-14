def bai2(k, n):
  if k == 0:
    return 1

  arr = []
  arr.append(3 % n)

  for i in range(1, k):
    arr.append(((arr[i - 1] * (3 % n)) % n))
  return arr[k - 1]


if __name__ == "__main__":
  k = 100000
  n = 123

  x = bai2(k, n)
  print(x)
