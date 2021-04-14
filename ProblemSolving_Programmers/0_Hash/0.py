import collections
# import defaultdict


def solution(participant, completion):
    comp = collections.Counter(completion)
    for man in participant:
        if comp[man] == 0:
            return man
        else:
            comp[man] -= 1


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer)[0]


a, b = ["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]
print(solution(a, b))
