a, b = map(int, input().split())


idx = 1  #리스트의 인덱스 기록
ls = [0] #수열(누적합) - 0을 기록하는 이유는 a와 b가 같을 수도 있기 때문에 a,b = 1,1 일 경우 오류 방지하기 위해서..! 
number = 1 #현재 수
cnt = 0 #현재 수가 몇번째 등장하는지
while idx <= b:
    ls.append(ls[-1]+number)
    cnt += 1
    if cnt == number:
        number += 1
        cnt = 0
    idx += 1
print(ls[b] - ls[a-1])