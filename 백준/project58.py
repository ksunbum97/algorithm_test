# 로봇을 좋아하는 세희는 로봇동아리에서 카메라와 센서, 라즈베리 파이, 집게발을 이용해 로봇을 완성하였다. 
# 이 로봇을 통해서 오셀로 재배치라는 작업을 하려고 한다. 오셀로 말은 앞면이 검정, 뒷면이 흰색으로 된 말이다. 
# 세희의 목표는 로봇을 이용하여 처음 배치된 오셀로 말을 주어진 형태로 바꾸는 일을 하는 것이다. 아래의 예시를 참고하자.
# 초기 상태	     목표 상태
#  ○●●○○ 	     ○●○●○
# 세희는 로봇을 이용해 2가지 작업 중 하나를 골라 진행할 수 있다.
# 배치된 말 중 임의의 2개의 말을 골라 서로의 위치를 바꾼다.
# 말 1개를 들어 뒤집어 놓아 색상을 변경한다.
# 위의 예시에서, 3번째와 4번째 말을 2번 작업을 통해 각각 뒤집으면 2번의 작업으로 목표 상태를 만들 수 있다. 하지만 1번 작업을 통해 3번째와 4번째 말을 골라 서로의 위치를 바꾸어주면 1번 만에 목표 상태에 도달할 수 있다. 초기 상태의 말과 목표 상태의 말이 주어질 때, 목표 상태에 도달할 수 있는 최소 횟수를 구하는 프로그램을 작성하시오.

# case = int(input())
# ans = []
# for _ in range(case):
#     n = int(input())
#     start = input()
#     end = input()
#     temp = []
#     cnt = 0
#     if start == end:
#         ans.append(cnt)
#     else:
#         if start.count('B') == end.count('B'): #임의의 두개를 옮기는 경우
#             for i in range(n):
#                 if start[i] == end[i]:
#                     continue
#                 else:
#                     if not temp:
#                         temp.append(start[i])
#                     else:
#                         del temp
#                         cnt+=1
#         else: #오셀로를 뒤집는 경우
#             for i in range(n):
#                 if start[i] != end[i]:
#                     cnt+=1
#         ans.append(cnt)

# for i in range(len(ans)):
#     print(ans[i])

from unittest import case


case = int(input())

answers = []
result = 0

for _ in range(case):
    arr = []
    N = int(input())
    start = input()
    goal = input()

    for i in range(N):
        if start[i] != goal[i]:
            arr.append(start[i])

    if arr.count("B") >= arr.count("W"):
        result = arr.count("B")
    else:
        result = arr.count("W")
    answers.append(result)

for answer in answers:
    print(answer)