
def histogram(arr):
    result = []
    for n in arr:
        l = len(result) - (n + 1)

        if l >= 0:
            result[n] += 1
        else:
            tmp = [0]*(-l)
            tmp[-1] = 1
            result += tmp
    
    return result

def getCost(hist, pos):
    cost = 0
    for i in range(len(hist)):
        cost += abs(pos - i)*hist[i]

    return cost

def getCost2(hist, pos):
    cost = 0
    for i in range(len(hist)):
        N = abs(pos - i)
        cost += 0.5*(N*(N+1))*hist[i]

    return cost
