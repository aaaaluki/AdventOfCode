


def parse(s:str) -> list:
    s = s.replace(' ', '')

    # If it's just a number return the number
    if s.isnumeric():
        return int(s)

    # If it's just a pair return a pair list
    if s.count(',') == 1:
        a, b = s[1:-1].split(',')

        return [int(a), int(b)]

    # Remove outer brackets
    s = s[1:-1]

    # Find the middle comma
    idx = 1
    count = 0
    for c in s:
        if c == '[':
            count += 1
        elif c == ']':
            count -= 1
        
        if count == 0:
            break
        
        idx += 1

    # Split on the middle comma and parse each side
    left_side = s[:idx]
    right_side = s[idx+1:]

    return [parse(left_side), parse(right_side)]


def reduce(l:list) -> list:
    while True:
        prev = l

        l = __explode(l, 0)
        l = __split(l)

        if l == prev:
            break
    
    return l
    

def addition(a:list, b:list) -> list:
    return [a, b]


def magnitude(l:list) -> int:
    
    if isinstance(l, int):
        return l

    return 3*magnitude(l[0]) + 2*magnitude(l[1])


def __explode(l:list, depth:int) -> list:
    return l


def __split(l:list) -> list:
    if isinstance(l, int):
        if l >= 10:
            a = l >> 1
            b = l - a
            return [a, b]
        else:
            return l

    return [__split(l[0]), __split(l[1])]
    

