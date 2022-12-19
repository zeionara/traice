from random import seed, uniform
from time import time, sleep

from traice import Traicer

traicer = Traicer()


def train_step():
    sleep(uniform(0, 1))


seed(17)

init_timestamp = time()

for i in range(1, 5):
    start_timestamp = time()
    train_step()
    traicer.push(i, uniform(0, 1 / i), (time_ := time()) - start_timestamp, time_ - init_timestamp)

print(traicer.df)
