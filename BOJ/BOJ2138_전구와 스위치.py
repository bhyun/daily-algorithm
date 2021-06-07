import sys
import copy

n = int(input())
cur = list(map(int, input()))
base = copy.deepcopy(cur)
target = list(map(int, input()))
answer = [sys.maxsize, sys.maxsize]

def switch(idx):
    if idx == 0:
        cur[idx] = 1 - cur[idx]
        cur[idx+1] = 1 - cur[idx+1]
    elif idx == len(cur)-1:
        cur[idx-1] = 1 - cur[idx-1]
        cur[idx] = 1 - cur[idx]
    else:
        cur[idx - 1] = 1 - cur[idx-1]
        cur[idx] = 1 - cur[idx]
        cur[idx + 1] = 1 - cur[idx+1]

# 첫번째 스위치 on
switch(0)
cnt = 1
for i in range(1, len(cur)):
    if cur[i-1] != target[i-1]:
        switch(i)
        cnt += 1

if cur == target:
    answer[0] = cnt

# 첫번째 스위치 off
cur = base
cnt = 0
for i in range(1, len(cur)):
    if cur[i-1] != target[i-1]:
        switch(i)
        cnt += 1

if cur == target:
    answer[1] = cnt

if answer[0] == sys.maxsize and answer[1] == sys.maxsize:
    print(-1)
else:
    print(min(answer))