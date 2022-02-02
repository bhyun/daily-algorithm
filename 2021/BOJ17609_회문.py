def search(word):
    left, right = 0, len(word)-1
    while left <= right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False # 일반 문자열
    return True # 유사회문


n = int(input())
for _ in range(n):
    word = input()
    left, right = 0, len(word) - 1
    flag = True
    while left <= right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            flag = False
            if search(word[left+1:right+1]) or search(word[left:right]):
                print(1)
                break
            else:
                print(2)
                break

    if flag:
        print(0)