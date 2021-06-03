from collections import defaultdict
n = int(input())
names = defaultdict(int)
answer = []
for _ in range(n):
    name = input()
    names[name[0]] += 1

for k, v in names.items():
    if v >= 5:
        answer.append(k)
answer.sort()

if not answer:
    print("PREDAJA")
else:
    print("".join(answer))