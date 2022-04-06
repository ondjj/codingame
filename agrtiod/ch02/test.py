def get_at(lst, index):
  if len(lst) == 0:
    return None
  if index < 0 or index > len(lst):
    return None
  return lst[index]

if __name__ == '__main__':

  x = [1,2]

  print(get_at(x,0))
  print(x[-1])

