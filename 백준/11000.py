# # 수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 
# # 김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 
# # 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
# # 수강신청 대충한 게 찔리면, 선생님을 도와드리자!

# 첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)
# 이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)

N = int(input()) 
C = [] 
end = [0] 
for i in range(N):
    C.append(list(map(int,input().split()))) 
C = sorted(C,key = lambda x: (x[0],x[1])) 
    
for i in range(N): 
    if C[i][0]>= min(end): 
        end.remove(min(end)) 
        end.append(C[i][1]) 
    else : 
        end.append(C[i][1]) 
print(len(end))
