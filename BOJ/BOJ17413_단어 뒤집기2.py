s = input()
answer = ""
parent_word = "" # 괄호 내부의 언어
word = "" # 그냥 단어
for idx, val in enumerate(s):
    if val == "<":
        answer += word[::-1]
        word = ""
        answer += "<"

    elif answer and answer[-1] == "<":
        if val == ">":
            answer += parent_word
            answer += ">"
            parent_word = ""
        else:
            parent_word += val

    elif val == " ":
        answer += word[::-1] + " "
        word = ""

    else:
        word += val
if word:
    answer += word[::-1]

print(answer)