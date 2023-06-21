def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for word in s:
        if not word.isdigit():
            return False
    return True
