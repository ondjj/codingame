def reorderLogFiles(self, logs: list[str]) -> list[str]:
  letters, digits = [], []
  for log in logs:
    if log.split()[1].isdigit():
      digits.append(log)
    else:
      letters.append(log)

  # 2개의 키를 람다 표현식으로 정렬
  letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits

# 람다 표현식 풀이
def func(x):

  return x.split()[1], x.split()[0]
  
  s.sort(key=func)

