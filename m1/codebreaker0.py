#!/usr/bin/env python3
import play
import numpy as np
import matplotlib.pyplot as plt
import codebreaker0
import codemaker1
import random
import common


def init():
    return


def codebreaker(evaluation_p):
    return ''.join(random.choices(common.COLORS, k=common.LENGTH))
