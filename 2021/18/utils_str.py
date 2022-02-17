import re

DEBUG = True


def parse(s: str) -> str:
    return s


def reduce(s: str) -> str:
    while True:
        prev = s
        s = __explode(s)
        s = __split(s)

        if s == prev:
            break
    return s


def addition(a: str, b: str) -> str:
    return '[{},{}]'.format(a, b)


def magnitude(s: str) -> int:
    return eval(s.replace(',', '+2*').replace('[', '(3*').replace(']', ')'))


def __explode(s: str) -> str:
    result = s

    c = 0
    for i in range(len(s)):
        if s[i].isnumeric():
            if c > 4:
                # Find where the pair ends
                for j in range(i + 1, len(s)):
                    if s[j] == ']':
                        break

                if not re.match(r'[0-9]+,[0-9]+', s[i:j]):
                    # Don't know if this is needed :^)
                    continue

                dist = j - i

                if s[i + dist - 1].isnumeric():
                    if DEBUG:
                        print('Exploding at {}:\t{}'.format(s[i:i + dist], s))

                    a, b = s[i:i + dist].split(',')
                    a = int(a)
                    b = int(b)

                    # Find left and right values, if any
                    left = None
                    values2left = re.finditer(r'[0-9]+', s[:i])
                    for left in values2left:
                        pass

                    right = None
                    values2right = re.finditer(r'[0-9]+', s[i + dist:])
                    for right in values2right:
                        break

                    # print('({},{})'.format(left.group(), right.group()))

                    # Left explosion
                    if left is not None:
                        result = s[:left.start()] + str(a + int(left.group())) + s[left.end():i - 1]
                    else:
                        result = s[:i - 1]

                    # Zero the middle
                    result += '0'

                    # Right explosion
                    if right is not None:
                        result += s[i + dist + 1:right.start() + i + dist] + str(b + int(right.group()))\
                                  + s[right.end() + i + dist:]
                    else:
                        result += s[i + dist:]

                    break

        else:
            if s[i] == '[':
                c += 1
            elif s[i] == ']':
                c -= 1

    return result


def __split(s: str) -> str:
    result = ''
    last_idx = 0
    for num_match in re.finditer('[0-9]+', s):
        if num_match.end() - num_match.start() > 1:
            num = int(num_match.group())
            a = num >> 1
            b = num - a

            result += s[last_idx:num_match.start()]
            result += '[{},{}]'.format(a, b)

            last_idx = num_match.end()

            if DEBUG:
                print('Splitting at {}:  \t{}'.format(num_match.group(), s))

            break
        else:
            result += s[last_idx:num_match.end()]
            last_idx = num_match.end()

    result += s[last_idx:]

    return result
