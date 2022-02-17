
def getKey(s:str):
    vals = s.split(' ')
    
    one = ''
    four = ''
    seven = ''
    digits = []
    segs = {'a':set(),
            'b':set(),
            'c':set(),
            'd':set(),
            'e':set(),
            'f':set(),
            'g':set()}
    
    for seg in vals:
        if len(seg) == 2:
            # Number one
            one = set(seg)

        elif len(seg) == 3:
            # Number seven
            seven = set(seg)

        elif len(seg) == 4:
            # Number four
            four = set(seg)

        elif len(seg) == 5:
            # Numbers 2, 3 or 5
            digits.append(set(seg))

        else:
            # The only digits needed for the calculation are 1, 4, 7 and
            # the 5 segment ones
            continue

    # Get the possible values for all the segments
    segs['a'] = seven.difference(one)
    segs['b'] = four.difference(one)
    segs['c'] = one
    segs['d'] = four.difference(one)
    segs['f'] = one

    remaining_segments = set('abcdefg').difference(one, seven, four)

    segs['e'] = remaining_segments
    segs['g'] = remaining_segments
    
    # Find number 3
    for d in digits:
        if d.intersection(one) == one:
            # The difference is going to be a set of size two containing the
            # segments d and g, since this two segments are independent we can
            # know the values of segments  b, d, e and g
            for s in d.difference(seven):
                if s in segs['d']:
                    tmp = segs['d']
                    segs['b'] = tmp.difference(s)
                    segs['d'] = set(s)
                else:
                    tmp = segs['g']
                    segs['e'] = tmp.difference(s)
                    segs['g'] = set(s)
    
    # Find number 2
    known_segments_two = set()
    for s in 'adeg':
        known_segments_two = known_segments_two.union(segs[s])

    for d in digits:
        seg_c = d.difference(known_segments_two)
        if len(seg_c) == 1:
            tmp = segs['c']
            segs['f'] = tmp.difference(seg_c)
            segs['c'] = seg_c

    # Transform list of sets to string
    key = ''
    for k in sorted(segs.keys()):
        key += segs[k].pop()

    return key


def getNum(numStr, key):
    # Decode a string of numbers separated by spaces
    nums = numStr.strip().split(' ')
    result = 0
    for n in nums:
        result = 10*result + decodeString(n, key)

    return result

def decodeString(num:str, key:str):
    # Decode a single number

    # First decode the string into the standard connections
    std_conns = 'abcdefg'
    connections = ''
    for c in num:
        connections += std_conns[key.index(c)]

    connections = ''.join(sorted(connections))
    
    if connections == 'abcefg':
        return 0
    elif connections == 'cf':
        return 1
    elif connections == 'acdeg':
        return 2
    elif connections == 'acdfg':
        return 3
    elif connections == 'bcdf':
        return 4
    elif connections == 'abdfg':
        return 5
    elif connections == 'abdefg':
        return 6
    elif connections == 'acf':
        return 7
    elif connections == 'abcdefg':
        return 8
    elif connections == 'abcdfg':
        return 9
    else:
        print(connections)
        raise Exception('LMAOOOOOO')
