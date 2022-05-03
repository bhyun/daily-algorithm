def solution(n, k, cmd):
    result = ["O"] * n

    dict = {}
    for i in range(n):
        if i == 0:
            dict[i] = [None, i + 1]
        elif i == n - 1:
            dict[i] = [i - 1, None]
        else:
            dict[i] = [i - 1, i + 1]

    stack = []

    for c in cmd:
        if c == "C":
            prev, next = dict[k]
            result[k] = "X"

            if prev == None:
                dict[next] = [None, dict[next][1]]
            elif next == None:
                dict[prev] = [dict[prev][0], None]
            else:
                dict[prev] = [dict[prev][0], next]
                dict[next] = [prev, dict[next][1]]

            stack.append((k, prev, next))

            if not next:
                k = prev
            else:
                k = next

        elif c == "Z":
            cur, prev, next = stack.pop()
            result[cur] = "O"

            if prev == None:
                dict[next] = [cur, dict[next][1]]
            elif next == None:
                dict[prev] = [dict[prev][0], cur]
            else:
                dict[prev] = [dict[prev][0], cur]
                dict[next] = [cur, dict[next][1]]

        else:
            command, x = c.split()
            x = int(x)

            cur = k

            if command == "U":
                while x > 0:
                    prev, next = dict[cur]
                    cur = prev
                    x -= 1
                k = cur

            elif command == "D":
                while x > 0:
                    prev, next = dict[cur]
                    cur = next
                    x -= 1
                k = cur

    return "".join(result)



print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))


