# 남극에 사는 김지민 선생님은 학생들이 되도록이면 많은 단어를 읽을 수 있도록 하려고 한다. 그러나 지구온난화로 인해 얼음이 녹아서 곧 학교가 무너지기 때문에, 김지민은 K개의 글자를 가르칠 시간 밖에 없다. 
# 김지민이 가르치고 난 후에는, 학생들은 그 K개의 글자로만 이루어진 단어만을 읽을 수 있다. 김지민은 어떤 K개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어의 개수가 최대가 되는지 고민에 빠졌다.
# 남극언어의 모든 단어는 "anta"로 시작되고, "tica"로 끝난다. 남극언어에 단어는 N개 밖에 없다고 가정한다. 학생들이 읽을 수 있는 단어의 최댓값을 구하는 프로그램을 작성하시오.
from sys import stdin
from itertools import combinations
from string import ascii_lowercase


n, k = map(int, stdin.readline().split())
words = []
# 각 입력 단어에 대하여
# 1. 앞의 anta와 뒤의 tica를 슬라이스한 뒤 set로 만들고
# 2. 그중 a/c/i/t/n을 제외한 뒤 words 리스트에 저장
for _ in range(n):
    words.append(set(stdin.readline().rstrip()[4:-4]).difference('a', 'c', 'i', 't', 'n'))

# a/c/i/t/n을 제외한 알파벳 모음
except_acitn = set(ascii_lowercase).difference('a', 'c', 'i', 't', 'n')
max_count = 0

if k < 5:
    print(0)

else:
    # a/c/i/t/n과 a/c/i/t/n을 제외한 알파벳 중 k - 5개를 고른 조합으로
    # 만들 수 있는 단어 개수의 최대값을 구한다.
    for x in list(combinations(except_acitn, k - 5)):
        count = 0
        for word in words:
            if not word.difference(x):
                count += 1

        max_count = max(max_count, count)

    print(max_count)