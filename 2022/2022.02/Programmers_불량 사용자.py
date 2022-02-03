answer = []

def search(user_id, target):
    temp = []
    for uid in user_id:
        if len(uid) == len(target):
            for u, t in zip(uid, target):
                if t == "*":
                    continue
                if u != t:
                    break
            else:
                temp.append(uid)
    return temp


def dfs(result, index, visited, target):
    global answer

    if len(visited) == target:
        visited.sort()
        if visited not in answer:
            answer.append(visited)
        return

    section = result[index]
    for i in range(len(section)):
        if section[i] not in visited:
            dfs(result, index + 1, visited + [section[i]], target)


def solution(user_id, banned_id):
    global answer
    result = []
    for bid in banned_id:
        result.append(search(user_id, bid))
    dfs(result, 0, [], len(banned_id))
    return len(answer)

# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))