from collections import deque
def solution(bridge_length, weight, truck_weights):
    # q => bridge_length만큼 [0]으로 초기화
    q = deque([0]) * bridge_length
    truck_weights = deque(truck_weights)
    tot = 0
    time = 0
    # 하나씩 빼고, 값을 넣는다.
    # 이때, 무게가 초과하면 넣지 않는다.
    while q and truck_weights:
        truck = q.popleft()
        tot -= truck
        if tot + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            q.append(truck)
            tot += truck
        else:
            q.append(0)

        time += 1

    # q에 트럭이 남아 있으면?
    time += len(q)
    return time