def solution(lines):
    answer = 0

    responses = []
    for line in lines:
        date, time, t = line.split()
        t = float(t[:-1]) * 1000

        hour, minute, second = time.split(":")
        endtime = (int(hour) * 3600 + int(minute) * 60 + float(second)) * 1000

        responses.append((endtime - t + 1, endtime))

    for standard_s, standard_e in responses:
        answer = max(answer, count(responses, standard_s, standard_s + 1000), count(responses, standard_e, standard_e + 1000))

    return answer

def count(responses, start, end):
    cnt = 0
    for s, e in responses:
        if e >= start and s < end:
            cnt += 1
    return cnt


print(solution( [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))

print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))

print(solution( [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))

