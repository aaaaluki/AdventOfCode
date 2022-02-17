import re

VERBOSE = False
NUM_PATTERN = re.compile(r'[0-9]+')


def add(snail_num1: str, snail_num2: str) -> str:
    return "[{},{}]".format(snail_num1, snail_num2)


def magnitude(snail_num: str) -> str:
    return eval(snail_num.replace('[', '(3*').replace(',', '+2*').replace(']', ')'))


def reduce(snail_num: str) -> str:
    while True:
        prev = snail_num
        while True:
            # I should learn how to read, this little loop has caused so much damage (because it was absent)
            prev_explosion = snail_num
            snail_num = __explode(snail_num)

            if prev_explosion == snail_num:
                break

        snail_num = __split(snail_num)

        if prev == snail_num:
            return snail_num


def __explode(snail_num: str) -> str:
    count = 0
    for i in range(len(snail_num)):
        c = snail_num[i]
        if not c.isnumeric():
            if c == '[':
                count += 1
            elif c == ']':
                count -= 1
            continue

        elif count > 4:
            # Find if it's a pair
            is_pair = False
            for j in range(i, len(snail_num)):
                if snail_num[j] == ']':
                    # It's a pair
                    is_pair = True
                    break
                elif snail_num[j] == '[':
                    # Not a pair
                    break

            if not is_pair:
                continue

            # It's a pair, explode
            left_idx = i - 1
            right_idx = j

            tmp = snail_num[left_idx + 1:right_idx].split(',')
            a, b = int(tmp[0]), int(tmp[1])

            # Find left and right numbers, if any
            left_num = None
            for m in re.finditer(NUM_PATTERN, snail_num[:left_idx]):
                left_num = m

            right_num = None
            for m in re.finditer(NUM_PATTERN, snail_num[right_idx:]):
                right_num = m
                break

            # Generate the resulting snail number
            if left_num is None:
                result = snail_num[:left_idx]
            else:
                result = snail_num[:left_num.start()] \
                         + str(int(left_num.group()) + a) \
                         + snail_num[left_num.end():left_idx]

            result += '0'

            if right_num is None:
                result += snail_num[right_idx + 1:]
            else:
                result += snail_num[right_idx + 1:right_num.start() + right_idx] \
                          + str(int(right_num.group()) + b) \
                          + snail_num[right_num.end() + right_idx:]

            if VERBOSE: print('Exploding at {}:\t{}'.format(snail_num[left_idx:right_idx + 1], snail_num))

            return result

    return snail_num


def __split(snail_num: str) -> str:
    for m in re.finditer(NUM_PATTERN, snail_num):
        num = int(m.group())
        if num >= 10:
            a = num >> 1
            b = num - a

            if VERBOSE: print('Splitting at {}:\t{}'.format(m.group(), snail_num))
            return snail_num[:m.start()] + '[{},{}]'.format(a, b) + snail_num[m.end():]

    return snail_num
