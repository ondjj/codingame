# 파이썬 다운 방식
def reverseString_py(self, s: list[str]) -> None:
  s.reverse()

# 풀이
def reverseString(self, s: list[str]) -> None:
  left, right = 0, len(s) - 1
  while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
