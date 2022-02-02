answer = 0

def dfs(numbers, target, idx, path):
    global answer

    if len(path) == len(numbers) and sum(path) == target:
        answer += 1
        return

    if len(numbers) <= idx + 1:
        return

    dfs(numbers, target, idx + 1, path + [numbers[idx + 1]])
    dfs(numbers, target, idx + 1, path + [-numbers[idx + 1]])


def solution(numbers, target):
    global answer

    dfs(numbers, target, 0, [numbers[0]])
    dfs(numbers, target, 0, [-numbers[0]])
    return answer