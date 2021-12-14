def distance(dic, k):
  d = {}
  for key, value in dic.items():
    dist = abs(dic[int(k)] - value)
    d[dist] = key
  return d

def deminingMines(file):
  with open(file, "r") as f:
    array = [0]
    l_dic = {}

    a = f.readline()
    arr = a.split()
    n = arr[0]
    t = arr[1]

    a = f.readline()
    l = a.split()
    for i in range(len(l)):
      l_dic[i + 1] = int(l[i])

    k = f.readline()
    d = distance(l_dic, k)
    d.pop(0)

    l_dic.pop(int(k))
    while len(l_dic) != 0:
      k = d[min(d)]
      array.append(min(d.keys()))
      d = distance(l_dic, k)
      d.pop(0)
      l_dic.pop(int(k))

    x = sum(array)
  with open('output.txt', "w") as output:
    output.write(str(x))
  return


if __name__ == "__main__":
  print(deminingMines("input.txt"))


