import numpy as np
import random
import common
import play
import matplotlib.pyplot as plt
import codebreaker1
import codemaker1
from itertools import product


def init():
    global l
    l = ["".join(combination) for combination in product(common.COLORS, repeat=common.LENGTH)]


def codebreaker(evaluation_p):
    global l
    eval = random.choice(l)
    l.remove(eval)
    return eval