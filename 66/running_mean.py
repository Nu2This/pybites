from statistics import mean
from decimal import Decimal

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    total = 0
    out = []
    for key, item in enumerate(sequence):
        total += item
        out.append(round(total / (key + 1), 2))
        print(total / (key + 1))
    print(out)
    return out
if __name__ == '__main__':
    running_mean([2, 6, 10, 8, 11, 10])
