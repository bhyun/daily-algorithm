def printAll(visited):
    result = ""
    for i in range(len(visited)):
        if visited[i]:
            result += string[i]
    if result:
        print(result)

def search(start, end):
    minIdx = -1
    minAlpha = ord('Z') + 1
    for i in range(start, end):
        if not visited[i] and ord(string[i]) < minAlpha:
            minIdx = i
            minAlpha = ord(string[i])

    if minIdx != -1:
        visited[minIdx] = True
        printAll(visited)
        search(minIdx, end)
        search(start, minIdx + 1)
    return

string = input()
visited = [False] * len(string)
search(0, len(string))

