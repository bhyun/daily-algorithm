def solution(numbers, hand):
    pos = {1: [0, 0], 2: [0, 1], 3: [0,2], 4: [1, 0], 5: [1,1], 6: [1,2], 7: [2,0], 8: [2,1], 9: [2,2], "*": [3, 0], 0: [3, 1], "#": [3, 2]}
    pair = {1: "L", 4: "L", 7: "L", 3: "R", 6: "R", 9: "R"}
    answer = ''
    left, right = pos["*"], pos["#"]
    for number in numbers:
        if number in pair.keys():
            answer += pair[number]
            if pair[number] == "L":
                left = pos[number]
            else:
                right = pos[number]
        else:
            ll = abs(left[0] - pos[number][0]) + abs(left[1] - pos[number][1])
            rr = abs(right[0] - pos[number][0]) + abs(right[1] - pos[number][1])
            if ll < rr:
                answer += "L"
                left = pos[number]
            elif ll > rr:
                answer += "R"
                right = pos[number]
            elif ll == rr:
                if hand == "left":
                    answer += "L"
                    left = pos[number]
                else:
                    answer += "R"
                    right = pos[number]
    return answer