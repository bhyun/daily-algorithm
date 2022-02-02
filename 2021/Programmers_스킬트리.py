def solution(skill, skill_trees):
    answer = len(skill_trees)
    for tree in skill_trees:
        prev = -1
        for s in skill:
            # 해당 스킬이 없는 경우
            if tree.find(s) == -1:
                idx = 100

            # 해당 스킬이 있는 경우
            if tree.find(s) != -1:
                idx = tree.index(s)

            if prev > idx:
                answer -= 1
                break
            prev = idx

    return answer