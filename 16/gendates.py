from datetime import datetime, timedelta
from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)
start = PYBITES_BORN


def gen_special_pybites_dates():
    y = 0
    while True:
        global PYBITES_BORN
        global start
        PYBITES_BORN += timedelta(days=100)
        if PYBITES_BORN - start > timedelta(days=365):
            y +=1
            start = start + timedelta(days=365)
            yield start
        yield PYBITES_BORN

       # yield PYBITES_BORN
#    global PYBITES_BORN
#    for i in range(n):

#        PYBITES_BORN += timedelta(days=100)
#        yield PYBITES_BORN


   # global start
   # out = start + timedelta(days=100)
   # for i in range(10):
   #     out += timedelta(days=100)

   #     yield out
   # pass

if __name__ == '__main__':
   # def runfunction():
   #     for x in range(10):
   #         gen_special_pybites_dates()

   # runfunction()
    gen = gen_special_pybites_dates()
    dates = list(islice(gen, 10))
    print(dates)
