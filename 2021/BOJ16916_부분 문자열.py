### TLE 발생
# s = input()
# p = input()
#
# idxs = []
# for i, sub in enumerate(s):
#     if sub == p[0]:
#         idxs.append(i)
#
# for idx in idxs:
#     if s[idx: idx+ len(p)] == p:
#         print(1)
#         break
# else:
#     print(0)


### 통과한 풀이
# import re
#
# s = input()
# p = input()
#
# pattern = re.compile(p)
# if pattern.search(s):
#     print(1)
# else:
#     print(0)


import re

pattern = re.compile("[a-z]+")
print(pattern.search("3 python"))
