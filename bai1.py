# Cau 1
import string

def findLongestString(s):
  new_string = s
  arr = []
  dic = {}
  whitespace = list(string.whitespace)
  punctuation = list(string.punctuation)
  delimiter = [x for x in punctuation]
  for i in whitespace:
    delimiter.append(i)
  
  count = 0
  for i in delimiter:
    a = s.count(i)
    count += a

  i = 0
  i_s = 0
  while True:
    if count == 0:
      arr.append(new_string)
      break
    
    else:
      if new_string[0] in delimiter:
        i_s += 1
        new_string = new_string[1:]
        count -= 1

      elif  new_string[i_s] not in delimiter:
        i_s += 1

      elif new_string[i_s] in delimiter:
        arr.append(new_string[0:i_s])
        new_string = new_string[i_s:]
        i_s = 0
    i += 1

  for i in arr:
    dic[len(i)] = i

  return len(dic[max(dic)])

if __name__ == "__main__":
  stringzz = "Oh…My god! 123help me(113) $ 123128391274aaa9127 *****123123asdasdasd ))))asdasd"
  x = findLongestString(stringzz)
  print(x)