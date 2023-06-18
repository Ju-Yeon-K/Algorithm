def solution(participants, completion):
    participants.sort()
    completion.sort()
    for i in range(len(completion)):
        if participants[i] != completion[i]:
            return participants[i]
    return participants[-1]