from datetime import datetime, timedelta
from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)
out = PYBITES_BORN


def gen_special_pybites_dates():

    global out

    out += timedelta(days=100)
    print(out.items())
    return out
    pass

if __name__ == '__main__':
    def runfunction():
        for x in range(10):
            gen_special_pybites_dates()

    runfunction()
