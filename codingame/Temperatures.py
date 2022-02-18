import sys
import math

min_t = 5527 # 온도의 범위가 -273 ~ 5526도이기 때문에 5527로 초기화
n = int(input()) # 숫자 입력 받음

if n == 0:  # 입력의 개수가 0이라면 0을 출력한다.
    min_t = "0"
else:
    for i in input().split(): # 입력 받는 숫자를 split을 통해 구분
        t = int(i) # input으로 들어오는 입력은 문자열로 인식 된다 int로 변경
        if abs(t) < abs(min_t): # 0으로부터 얼마나 가까운지에 따라 출력 될 값이 결정 되므로 abs 함수를 통해 절댓값으로 치환
            min_t = t
        if abs(t) == abs(min_t): # 두 수의 절댓값이 같다면 양수를 출력하기 위해 비교
            if t > 0:
                min_t = t
print(min_t)

# min_t에 값이 저장되기 때문에 대소 비교를 용이하게 할 수 있다.