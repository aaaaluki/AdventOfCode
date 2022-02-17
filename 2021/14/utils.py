
from collections import defaultdict
from math import ceil
from typing import Dict


def step(state:str, rules:Dict[str, str]):
    
    result = ''
    for i in range(len(state) - 1):
        result += state[i]
        
        if state[i:i+2] in rules.keys():
            result += rules[state[i:i+2]]
    
    return result + state[-1]


def fast_step(histo:Dict[str, int], rules:Dict[str, str]) -> Dict[str, int]:

    result = histo.copy()
    for (a, b), v in histo.items():
        if a+b in rules and v > 0:
            mid = rules[a+b]

            result[a + b]   -= v
            result[a + mid] += v
            result[mid + b] += v


    return result

def pair_histogram(s:str) -> Dict[str, int]:
    
    d = defaultdict(int)
    for i in range(len(s) - 1):
        d[s[i:i+2]] += 1

    return d


def count_elements(histo:Dict[str, int]) -> Dict[str, int]:
    counter = defaultdict(int)

    for k, v in histo.items():
        counter[k[0]] += v*0.5
        counter[k[1]] += v*0.5
    
    for k, v in counter.items():
        counter[k] =  ceil(v)

    return counter
