# 상근이는 한국 최고의 가수를 뽑는 "나는 위대한 슈퍼스타K"의 감독이다. 상근이는 다음과 같이 참가자를 선발하려고 한다.
# "나는 위대한 슈퍼스타K"의 예선에는 N명이 참가했고, 서로 다른 M개 장르에 대한 오디션을 보았다. 심사위원은 모든 참가자의 각 장르에 대한 능력을 점수로 매겼다. 이 점수는 실수로 나타낸다.
# 본선에는 총 K명이 나갈 수 있다. 각 참가자는 본선에서 단 하나의 장르만 부를 수 있고, 이 장르는 상근이가 정해준다. 한 사람이 여러 장르를 부를 수는 없지만, 여러 사람이 같은 장르를 부를 수는 있다.
# 모든 참가자의 각 장르에 대한 능력이 주어진다. 이때, 능력의 합이 최대가 되도록 참가자와 장르를 선택하는 프로그램을 작성하시오.

import sys
N, M, K = map(int, sys.stdin.readline().split())

candidate_score = {}
for i in range(N):
    candidate_score[i+1] = 0

for i in range(M):
    genre = list(map(float, sys.stdin.readline().split()))
    for j in range(0, 2*N, 2):
        if genre[j+1] > candidate_score[genre[j]]:
            candidate_score[genre[j]] = genre[j+1]

score = sorted(list(candidate_score.values()), reverse=True)
sum = sum(score[:K])
print('%.1f' % sum)