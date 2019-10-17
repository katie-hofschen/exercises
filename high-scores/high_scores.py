def latest(scores):
    return scores[-1]

def personal_best(scores):
    res = sorted(scores, reverse=True)[0]
    return res

def personal_top_three(scores):
    return sorted(scores, reverse=True)[0:3]



