def solution(rows, columns, queries):
    result = []
    num = 1
    graph = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(num)
            num += 1
        graph.append(row)

    for query in queries:
        x1, y1, x2, y2 = query
        one = []
        two = []
        three = []
        four = []
        for i in range(y1 - 1, y2 - 1):
            one.append(graph[x1 - 1][i])
        minVal = min(one)
        for i in range(x1 - 1, x2 - 1):
            two.append(graph[i][y2 - 1])
        minVal = min(minVal, min(two))
        for i in range(y1, y2):
            three.append(graph[x2 - 1][i])
        minVal = min(minVal, min(three))
        for i in range(x1, x2):
            four.append(graph[i][y1 - 1])
        minVal = min(minVal, min(four))
        two.insert(0, one.pop())
        three.append(two.pop())
        four.append(three.pop(0))
        one.insert(0, four.pop(0))

        print(one, two, three, four)

        for i in range(len(one)):
            graph[x1 - 1][y1 - 1 + i] = one[i]
        for i in range(len(two)):
            graph[x1 - 1 + i][y2 - 1] = two[i]
        for i in range(len(three)):
            graph[x2-1][y1 + i] = three[i]
        for i in range(len(four)):
            graph[x1 + i][y1 - 1] = four[i]
        result.append(minVal)
        print("graph: ", graph)
    return result

